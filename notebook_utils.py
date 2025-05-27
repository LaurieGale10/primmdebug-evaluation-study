from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from pandas import DataFrame

#Necessary rpy2 imports
from rpy2.robjects.packages import importr, data
from sklearn.metrics import pairwise_distances
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri, numpy2ri, conversion, default_converter
from rpy2.robjects.vectors import StrVector

utils = importr('utils')
utils.install_packages(StrVector('WeightedCluster'))



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
    average_silhouette_width = cluster_quality_result[0][4]
    huberts_c = cluster_quality_result[0][9]
    return {
        "point_biserial_correlation": point_biserial_correlation,
        "average_silhouette_width": average_silhouette_width,
        "huberts_c": huberts_c
    }