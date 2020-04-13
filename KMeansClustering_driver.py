""" Step 4 Driver """
""" Otto Laakso """

import KMeansClustering_functions as kmc 

k = 2  
glucose, hemoglobin, classification = kmc.openckdfile()
glucose_scaled, hemoglobin_scaled, classification = kmc.normalizeData(glucose, hemoglobin, classification)
centroid_array, new_classes = kmc.kMeansClustering(k, glucose_scaled, hemoglobin_scaled)

unscaled_centroids = kmc.unscaledCentroids(centroid_array)
kmc.graphingKMeans(glucose, hemoglobin, new_classes, unscaled_centroids)