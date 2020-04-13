Project 2
Otto Laakso

This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Folder Contents:
- ckd.txt - Training data used in the project
- NearestNeighborClassification.py - Code for Step 2 and 3 of the project
- KMeansClustering_functions.py - Functions for Step 4 of the project
- KMeansClustering_driver.py - Driver for Step 4 of the project
- README.md - instructions for running the contents of the folder

K Means Clustering Functions:

openckdfile():
- Takes no parameters
- Opens the file "ckd.txt" and separates glucose, hemoglobin, and classification values
- Returns glucose, hemoglobin, and classification in separate lists

def normalizeData(glucose, hemoglobin, classification):
- Takes glucose, hemoglobin, and classification lists as parameters
- Normalizes each value of glucose and hemoglobin to fit a 0-1 scale
- Returns normalized arrays glucose_scaled, hemoglobin_scaled, and classification

def initialCentroids(k):
- Takes the number of centroids, k, as a parameter
- Assigns a random value for glucose and hemoglobin for each centroid, on a 0-1 scale
- Assigns a classification for each centroid and returns the array of scaled centroids

def calculateDistanceArray(centroid_array, glucose_value, hemoglobin_value):
- Takes an array of centroids, a glucose value, and a hemoglobin value as parameters
- Calculates the distance between the (hemoglobin, glucose) point and each centroid
- Returns an array of the calculated distances
    
def kMeansClustering(k, glucose_scaled, hemoglobin_scaled):
- Takes the number of clusters and the arrays of scaled glucose and hemoglobin values as parameters
- Performs K Means Clustering by iterating through the assign-update steps
- Returns an array of final centroid locations and an array of assigned classifications

def unscaledCentroids(centroid_array):
- Takes an array of centroids as a parameter
- Converts the normalized values to the inital glucose and hemoglobin scales
- Returns an array of unscaled centroids

def graphingKMeans(glucose, hemoglobin, new_classes, unscaled_centroids):
- Takes arrays of glucose and hemoglobin values, assigned classifications, and unscaled centroids as parameters
- Graphs the centroids and the clusters and labels their classifications
- Returns None
    




