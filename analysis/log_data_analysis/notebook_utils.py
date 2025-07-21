from statistics import median
import numpy as np
from pandas import DataFrame
import plotly.express as px

from analysis.log_data_analysis.classes.exercise_log import ExerciseLog
from analysis.log_data_analysis.classes.processors.exercise_log_processor import ExerciseLogProcessor
from analysis.log_data_analysis.classes.processors.stage_log_processor import StageLogProcessor
from analysis.log_data_analysis.enums import DebuggingStage
from analysis.log_data_analysis.testing_service.test_report import TestReport

def display_percentage_string(x: int | float, y: int | float, decimal_places: int = 2) -> str:
    """Display a percentage string in the form 'x/y (percentage%)'"""
    if y == 0:
        return f"{x}/{y} (N/A)"
    percentage: float = (x / y) * 100
    return f"{x}/{y} ({percentage:.{decimal_places}f}%)"

def is_one_indexed(cluster_labels: list[int]) -> bool:
    return all(label >= 1 for label in cluster_labels)

def get_size_of_clusters(cluster_labels: list[int]) -> dict[int, int]:
    items_per_cluster = {i + 1: 0 for i in range(min(cluster_labels), max(cluster_labels) + 1)}
    for label in cluster_labels:
        items_per_cluster[label + 1] += 1
    return items_per_cluster

def plot_session_data_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    plotting_data = {"cluster": [], "session": [], "count": []}
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        session_counts: dict[str, int] = {j: 0 for j in range(1, 7)}
        for exercise_log in exercise_logs_in_cluster:
            session_counts[exercise_log.session] += 1
        for session, count in session_counts.items():
            plotting_data["cluster"].append(str(i))
            plotting_data["session"].append(str(session))
            plotting_data["count"].append(count)
    plotting_data_df: DataFrame = DataFrame(plotting_data)
    px.bar(
        plotting_data_df,
        x="session",
        y="count",
        color="cluster",
        barmode="group",
        title="Number of sessions per cluster" if model_name is None else f"Number of PRIMMDebug challenges per session per cluster ({model_name})"
    ).show()

def plot_histogram_times_per_exercise_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    exercise_logs_clusters_mapping["time_per_challenge"] = [0 for i in range(len(exercise_logs_clusters_mapping))]
    for idx, row in exercise_logs_clusters_mapping.iterrows():
        exercise_log: ExerciseLog = ExerciseLogProcessor.get_exercise_log_by_id(row["exercise_log_id"], exercise_logs)
        if exercise_log is not None:
            exercise_logs_clusters_mapping.at[idx, "time_per_challenge"] = ExerciseLogProcessor.get_time_on_exercise(exercise_log)
    px.histogram(
        exercise_logs_clusters_mapping,
        x="time_per_challenge",
        color="cluster",
        title="Time spent on each PRIMMDebug challenge" if model_name is None else f"Time spent on each PRIMMDebug challenge ({model_name})",
        labels={"time_per_challenge": "Time (seconds)", "cluster": "Cluster"},
        nbins=20,
        marginal="box"
    ).show()

def plot_median_times_per_exercise_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
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
        title="Median time spent on each PRIMMDebug challenge per cluster" if model_name is None else f"Median time spent on each PRIMMDebug challenge per cluster ({model_name})"
    ).show()

def plot_histogram_times_per_stage_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
    columns: list[DebuggingStage] = [DebuggingStage.predict, DebuggingStage.run, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.find_error, DebuggingStage.fix_error, DebuggingStage.test]
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        #Stage, time
        plotting_data: DataFrame = DataFrame(columns=["stage", "time"])
        for log in exercise_logs_in_cluster:
            times_per_stage = ExerciseLogProcessor.get_time_per_stage(log)
            for stage, time in times_per_stage.items():
                if stage in columns:
                    plotting_data.loc[len(plotting_data)] = {"stage": stage, "time": time}
        px.histogram(
            plotting_data,
            x="time",
            color="stage",
            title=f"Time spent on each PRIMMDebug stage in cluster {i} (n={len(exercise_logs_in_cluster)})" if model_name is None else f"Time spent on each PRIMMDebug stage in cluster {i} ({model_name}, n={len(exercise_logs_in_cluster)})",
            labels={"time": "Time (seconds)", "stage": "Stage"},
            nbins=20,
            marginal="box"
        ).show()

def plot_median_times_per_stage_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    plotting_data = {"cluster": [], "stage": [], "time": []}
    columns: list[DebuggingStage] = [DebuggingStage.predict, DebuggingStage.run, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.find_error, DebuggingStage.fix_error, DebuggingStage.test]
    for i in range(1, max(exercise_logs_clusters_mapping["cluster"]) + 1):
        exercise_logs_in_cluster = [log for log in exercise_logs if log.id in exercise_logs_clusters_mapping.loc[exercise_logs_clusters_mapping["cluster"] == i, "exercise_log_id"].tolist()]
        for stage in columns:
            median_time_per_stage: float = median([StageLogProcessor.get_time_on_stage(stage_log) for exercise_log in exercise_logs_in_cluster for stage_log in exercise_log.stage_logs if stage_log.stage_name == stage])
            plotting_data["cluster"].append(str(i))
            plotting_data["stage"].append(stage.value)
            plotting_data["time"].append(median_time_per_stage)
    plotting_data_df: DataFrame = DataFrame(plotting_data)
    px.bar(
        plotting_data_df,
        x="stage",
        y="time",
        color="cluster",
        barmode="group",
        title="Median time spent on each PRIMMDebug stage per cluster" if model_name is None else f"Median time spent on each PRIMMDebug stage per cluster ({model_name})"
    ).show()

def plot_median_times_per_stage_of_cluster_centroids(cluster_centroids: DataFrame, model_name: str = None):
    cluster_centroids_long = cluster_centroids.reset_index().melt(
        id_vars="index",
        var_name="stage",
        value_name="time"
    ).rename(columns={"index": "cluster"})
    cluster_centroids_long["cluster"] = cluster_centroids_long["cluster"].astype(str)
    px.bar(cluster_centroids_long, x="stage", y="time", color="cluster", barmode="group", title=f"Estimated means {model_name}").show()

def plot_histogram_number_of_stages(exercise_logs_clusters_mapping: list[ExerciseLog], exercise_logs: list[ExerciseLog], model_name: str = None):
    if not is_one_indexed(exercise_logs_clusters_mapping["cluster"].tolist()):
        raise ValueError("The 'cluster' column in exercise_logs_clusters_mapping must be one-indexed.")
    
    exercise_logs_clusters_mapping["number_of_stages"] = [0 for i in range(len(exercise_logs_clusters_mapping))]
    for idx, row in exercise_logs_clusters_mapping.iterrows():
        exercise_log: ExerciseLog = ExerciseLogProcessor.get_exercise_log_by_id(row["exercise_log_id"], exercise_logs)
        if exercise_log is not None:
            exercise_logs_clusters_mapping.at[idx, "number_of_stages"] = len(exercise_log.stage_logs)
    px.histogram(
        exercise_logs_clusters_mapping,
        x="number_of_stages",
        color="cluster",
        title="Number of stages per PRIMMDebug challenge" if model_name is None else f"Number of stages per PRIMMDebug challenge ({model_name})",
        labels={"number_of_stages": "Number of Stages", "cluster": "Cluster"},
        nbins=20,
        marginal="box"
    ).show()

def plot_median_number_of_stages_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None):
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
        title="Median number of stages per PRIMMDebug challenge per cluster" if model_name is None else f"Median number of stages per PRIMMDebug challenge per cluster ({model_name})",
    ).show()

def plot_correctness_of_clusters(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None) -> DataFrame:
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
        title="Percentage of successful PRIMMDebug challenge attempts for each cluster" if model_name is None else f"Percentage of successful PRIMMDebug challenge attempts for each cluster ({model_name})"
    ).show()

def plot_cluster_visualisations(exercise_logs_clusters_mapping: DataFrame, exercise_logs: list[ExerciseLog], model_name: str = None, cluster_centroids: DataFrame = None):
    plot_correctness_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)
    
    plot_median_number_of_stages_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)
    plot_histogram_number_of_stages(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)
    
    if cluster_centroids is not None:
        plot_median_times_per_stage_of_cluster_centroids(cluster_centroids, model_name=model_name)
    else:
        plot_median_times_per_stage_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name, cluster_centroids=cluster_centroids)
    plot_histogram_times_per_stage_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)
    
    plot_median_times_per_exercise_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)
    plot_histogram_times_per_exercise_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)

    plot_session_data_of_clusters(exercise_logs_clusters_mapping, exercise_logs, model_name=model_name)

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