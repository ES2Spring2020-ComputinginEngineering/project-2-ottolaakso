Project 2
Otto Laakso

This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Folder Contents:
- ckd.txt - Training data used in the project
- NearestNeighborClassification.py - Code for Step 2 and 3 of the project
- KMeansClustering_functions.py - Functions for Step 4 of the project
- KMeansClustering_driver.py - Driver for Step 4 of the project
- README.md - instructions for running the contents of the folder

Nearest Neighbour & K Nearest Neighbour Functions:

To run the code, assign a value for k in the "Main Code" section and click "Run".

def openckdfile():
- Takes no parameters
- Opens the file "ckd.txt" and separates glucose, hemoglobin, and classification values
- Returns glucose, hemoglobin, and classification in separate lists

def normalizeData(glucose, hemoglobin, classification):
- Takes glucose, hemoglobin, and classification lists as parameters
- Normalizes each value of glucose and hemoglobin to fit a 0-1 scale
- Returns normalized arrays glucose_scaled, hemoglobin_scaled, and classification (not changed)

def graphData(glucose, hemoglobin, classification):
- Takes the original glucose, hemoglobin, and classification values
- Graphs hemoglobin vs. glucose values and classifies them
- Void function

def createTestCase():
- Takes no parameters
- Creates a random glucose value (newg) and a random hemoglobin value (newh)
- Creates normalized versions of newg (newglucose) and newh (newhemoglobin)
- Returns newg, newh, newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled):
- Takes the random glucose and hemoglobin values and the scaled glucose and hemoglobin arrays
- Calculates the distance between the random (glucose, hemoglobin) point for each training set point
- Returns an array of the calculated distances

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
- Takes newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, and classification as parameters
- Determines the classification of the training data point closest to the random test point
- Returns the classification of the nearest training data point

def graphTestCase(newg, newh, glucose, hemoglobin, classification):
- Takes the randomly generated glucose and hemoglobin values as well as the training data as parameters
- Plots the test case in comparison to the training data
- Returns None

def kNearestNeighborsClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
- Takes the number of points (k), newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, and classification as parameters
- Finds the classifications of k closest points to the test case
- Returns the median value of the k classifications


K Means Clustering Functions:

To run the code, assign a value for k in KMeansClustering_driver.py and click "Run".

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
    




