""" Step 2 & 3 Code """
""" Otto Laakso """

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def openckdfile():
# Takes no parameters
# Opens the file "ckd.txt" and separates glucose, hemoglobin, and classification values
# Returns glucose, hemoglobin, and classification in separate lists
    glucose, hemoglobin, classification = np.loadtxt('ckd.txt', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
# Takes glucose, hemoglobin, and classification lists as parameters
# Normalizes each value of glucose and hemoglobin to fit a 0-1 scale
# Returns normalized arrays glucose_scaled, hemoglobin_scaled, and classification (not changed)
    
    g_list = []
    h_list = []
    
    for line in glucose:
        g_scaled = (line-70)/(490-70)
        g_list.append(g_scaled)
    
    for line in hemoglobin:
        h_scaled = (line-3.1)/(17.8-3.1)
        h_list.append(h_scaled)
    
    glucose_scaled = np.array(g_list)
    hemoglobin_scaled = np.array(h_list)
    classification = np.array(classification)

    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
# Takes the original glucose, hemoglobin, and classification values
# Graphs hemoglobin vs. glucose values and classifies them
# Void function
    
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "b.", label = "Class = 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class = 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin vs. Glucose Correlation for CKD Patients")
    plt.grid(True)
    plt.legend()
    plt.show()
    
def createTestCase():
# Takes no parameters
# Creates a random glucose value (newg) and a random hemoglobin value (newh)
# Creates normalized versions of newg (newglucose) and newh (newhemoglobin)
# Returns newg, newh, newglucose, newhemoglobin
    
    newg = random.randint(69,491)
    newh = random.uniform(3.1, 17.8)
    
    newglucose = (newg-70)/(490-70)
    newhemoglobin = (newh-3.1)/(17.8-3.1)
    
    return newg, newh, newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled):
# Takes the random glucose and hemoglobin values and the scaled glucose and hemoglobin arrays
# Calculates the distance between the random (glucose, hemoglobin) point for each training set point
# Returns an array of the calculated distances
    
    distance = []
    
    for line in range(len(glucose_scaled)):
        d = math.sqrt((newglucose - glucose_scaled[line])**2 + (newhemoglobin - hemoglobin_scaled[line])**2)
        distance.append(d)
    
    distance_array = np.array(distance)
    
    return distance_array

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
# Takes newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, and classification as parameters
# Determines the classification of the training data point closest to the random test point
# Returns the classification of the nearest training data point
    
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    
    min_index = np.argmin(distance_array)
    nearest_class = classification[min_index]
    
    return nearest_class

def graphTestCase(newg, newh, glucose, hemoglobin, classification):
# Takes the randomly generated glucose and hemoglobin values as well as the training data as parameters
# Plots the test case in comparison to the training data
# Returns None
    
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "b.", label = "Class = 1.0")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "y.", label = "Class = 0.0")
    plt.plot(newh, newg, "r^", label = "Test Case")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Test Case for CKD")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    return

def kNearestNeighborsClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
# Takes the number of points (k), newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, and classification as parameters
# Finds the classifications of k closest points to the test case
# Returns the median value of the k classifications
    
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
    
    sorted_indices = np.argsort(distance_array)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]

    k_class = np.median(k_classifications)
    
    return k_class

# Main Code
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
newg, newh, newglucose, newhemoglobin = createTestCase()
k = 3

graphData(glucose, hemoglobin, classification)
calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
graphTestCase(newg, newh, glucose, hemoglobin, classification)
nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)
kNearestNeighborsClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)


