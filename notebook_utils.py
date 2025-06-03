from statistics import median
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from pandas import DataFrame
import plotly.express as px

from classes.exercise_log import ExerciseLog
from classes.processors.exercise_log_processor import ExerciseLogProcessor
from classes.processors.stage_log_processor import StageLogProcessor
from enums import DebuggingStage
from testing_service.test_report import TestReport


def display_percentage_string(x: int | float, y: int | float, decimal_places: int = 2) -> str:
    """Display a percentage string in the form 'x/y (percentage%)'"""
    if y == 0:
        return f"{x}/{y} (N/A)"
    percentage: float = (x / y) * 100
    return f"{x}/{y} ({percentage:.{decimal_places}f}%)"

def plot_silhouette_plot(cluster_labels, silhouette_values, silhouette_score, n_clusters):
    fig, ax = plt.subplots()

    y_lower = 10
    for i in range(n_clusters):
        ith_cluster_silhouette_values = silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        # Label the silhouette plots with their cluster numbers at the middle
        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples
    ax.axvline(x=silhouette_score, color="red", linestyle="--")
    return fig, ax

def is_one_indexed(cluster_labels: list[int]) -> bool:
    return all(label >= 1 for label in cluster_labels)

def plot_median_times_per_exercise(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog]):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    median_times_per_exercise_per_cluster: list[float] = []
    plotting_data: DataFrame = DataFrame({"cluster": [str(i) for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1)]}) #Converted to string to avoid plotting this as a continuous variable
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        median_times_per_exercise_per_cluster.append(median([ExerciseLogProcessor.get_time_on_exercise(log) for log in exercise_logs_in_cluster]))
    plotting_data.insert(1, "median_time", median_times_per_exercise_per_cluster)
    px.bar(
        plotting_data,
        x="cluster",
        y="median_time",
        title="Median time spent on each PRIMMDebug challenge per cluster"
    ).show()

def plot_median_times_per_stage_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], cluster_centroids: DataFrame = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    plotting_data = {"cluster": [], "stage": [], "time": []}
    columns: list[DebuggingStage] = [DebuggingStage.predict, DebuggingStage.run, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.find_error, DebuggingStage.fix_error, DebuggingStage.test]
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        for stage in columns:
            if cluster_centroids is not None and stage.value not in cluster_centroids.columns:
                plotting_data["time"].append(cluster_centroids[stage.value].iloc[i]) #TODO: Test this is working
            else:
                median_time_per_stage: float = median([StageLogProcessor.get_time_on_stage(stage_log) for exercise_log in exercise_logs_in_cluster for stage_log in exercise_log.stage_logs if stage_log.stage_name == stage])
                plotting_data["cluster"].append(str(i))
                plotting_data["stage"].append(stage.value)
                plotting_data["time"].append(median_time_per_stage)
    plotting_data_df: DataFrame = DataFrame(plotting_data)
    px.bar(plotting_data_df, x="stage", y="time", color="cluster", barmode="group", title="Median time spent on each PRIMMDebug stage per cluster").show()

def plot_median_number_of_stages_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], cluster_centroids: DataFrame = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    plotting_data: DataFrame = DataFrame({"cluster": [str(i) for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1)]})
    median_number_of_stages_per_cluster: list[int] = []
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        median_number_of_stages_per_cluster.append(median([len(exercise_log.stage_logs) for exercise_log in exercise_logs_in_cluster]))
    plotting_data.insert(1, "median_number_stages", median_number_of_stages_per_cluster)
    px.bar(
        plotting_data,
        x="cluster",
        y="median_number_stages",
        title="Median number of stages per PRIMMDebug challenge per cluster"
    ).show()

def plot_correctness_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog]) -> DataFrame:
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    plotting_data: DataFrame = DataFrame({"cluster": [str(i) for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1)]})
    percent_success_per_cluster: list[int] = []
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        test_reports_in_cluster: list[TestReport] = [exercise_log._test_report for exercise_log in exercise_logs_in_cluster if exercise_log._test_report is not None]
        successful_attempts: int = len([test_report for test_report in test_reports_in_cluster if test_report.n_successful_tests == test_report.n_total_tests]) 
        percent_success_per_cluster.append((successful_attempts / len(test_reports_in_cluster)) * 100 if len(test_reports_in_cluster) > 0 else 0)
    plotting_data.insert(1, "percent_success", percent_success_per_cluster)
    px.bar(
        plotting_data,
        x="cluster",
        y="percent_success",
        title="Percentage of successful PRIMMDebug challenge attempts for each cluster"
    ).show()

def prepare_cluster_plots(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], cluster_centroids: DataFrame = None):
    plot_correctness_of_clusters(exercise_logs_clusters_mapping, exercise_logs)
    plot_median_number_of_stages_of_clusters(exercise_logs_clusters_mapping, exercise_logs, cluster_centroids)
    plot_median_times_per_stage_of_clusters(exercise_logs_clusters_mapping, exercise_logs, cluster_centroids)
    plot_median_times_per_exercise(exercise_logs_clusters_mapping, exercise_logs)

"""
#Necessary rpy2 imports
from rpy2.robjects.packages import importr
from sklearn.metrics import pairwise_distances
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri, numpy2ri, conversion, default_converter
from rpy2.robjects.vectors import StrVector

utils = importr('utils')
utils.install_packages(StrVector('WeightedCluster'))


def calculate_cluster_evaluation_metrics(df: DataFrame, cluster_labels: np.ndarray | list[int], distance_metric = "euclidean") -> DataFrame:
    weightedcluster_library = importr('WeightedCluster')
    dissimilarity_matrix = pairwise_distances(df, metric="euclidean")
    with (ro.default_converter + numpy2ri.converter).context():
        # Convert to R matrix
        diss_r = conversion.get_conversion().py2rpy(dissimilarity_matrix)
        cluster_labels_r = conversion.get_conversion().py2rpy(cluster_labels + 1)  # R uses 1-based indexing
        cluster_quality_result = weightedcluster_library.wcClusterQuality(
            diss_r,
            cluster_labels_r
        )
    point_biserial_correlation = cluster_quality_result[0][0]
    average_silhouette_width = cluster_quality_result[0][3]
    huberts_c = cluster_quality_result[0][9]
    return {
        "point_biserial_correlation": point_biserial_correlation,
        "average_silhouette_width": average_silhouette_width,
        "huberts_c": huberts_c
    }
"""