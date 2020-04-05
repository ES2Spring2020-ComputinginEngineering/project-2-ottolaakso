""" Step 2 & 3 Code """
""" Otto Laakso """

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.txt', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    
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
    
    newglucose = random.randint(69,491)
    newhemoglobin = random.uniform(3.1, 17.8)
    
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled):
    
    distance = []
    
    for line in range(len(glucose_scaled)):
        d = math.sqrt((newglucose - glucose_scaled[line])**2 + (newhemoglobin - hemoglobin_scaled[line])**2)
        distance.append(d)
    
    distance_array = np.array(distance)
    
    return distance_array

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
    
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    
    min_index = np.argmin(distance_array)
    nearest_class = classification[min_index]
    print(nearest_class)
    
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "b.", label = "Class = 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "y.", label = "Class = 0")
    plt.plot(newhemoglobin, newglucose, "rx")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Test Case for CKD")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    return

def kNearestNeighborsClassifier(k, newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification):
    
    distance_array = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    
    sorted_indices = np.argsort(distance_array)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    
    return k_classifications

glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
newglucose, newhemoglobin = createTestCase()

graphData(glucose, hemoglobin, classification)

calculateDistanceArray(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled)
nearestNeighborClassifier(newglucose, newhemoglobin, glucose_scaled, hemoglobin_scaled, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    