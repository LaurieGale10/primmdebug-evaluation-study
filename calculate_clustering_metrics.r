    calculate_cluster_evaluation_metrics <- function(df, cluster_labels, distance_metric = "euclidean") {
        if (!requireNamespace("WeightedCluster", quietly = TRUE)) {
            install.packages("WeightedCluster")
        }
        suppressPackageStartupMessages(library(WeightedCluster))
        
        # Compute dissimilarity matrix
        diss_matrix <- as.matrix(dist(df, method = distance_metric))
        # R uses 1-based indexing, so cluster_labels should already be correct
        cluster_quality_result <- wcClusterQuality(diss_matrix, cluster_labels)
        
        point_biserial_correlation <- cluster_quality_result$stats[1]
        average_silhouette_width <- cluster_quality_result$stats[4]
        huberts_c <- cluster_quality_result$stats[10]
        
        return(list(
            point_biserial_correlation = point_biserial_correlation,
            average_silhouette_width = average_silhouette_width,
            huberts_c = huberts_c
        ))
    }