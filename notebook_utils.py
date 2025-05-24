from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

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