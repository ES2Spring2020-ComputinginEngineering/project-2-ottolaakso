""" Step 4 Code """
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

def initialCentroids(k):
    
    glucose, hemoglobin, classification = openckdfile()
    scaled_centroids = []
    
    for i in range(k):
        
        g = random.uniform(0,1)
        h = random.uniform(0,1)
        centroid_k = [g, h, i]
        scaled_centroids.append(centroid_k)
  
    centroid_array = np.array(scaled_centroids)
    
    return centroid_array

def calculateDistanceArray(centroid_array, glucose_value, hemoglobin_value):
    
    distance = []
    
    for i in range(len(centroid_array)):
        centroid = centroid_array[i]

        d = math.sqrt((centroid[0] - glucose_value)**2 + (centroid[1] - hemoglobin_value)**2)
        distance.append(d)

    distance_array = np.array(distance)
    
    return distance_array

def kMeansClustering(k, glucose_scaled, hemoglobin_scaled):
    """ This function seems to work for k<3 and I can't figure out why """    
    iteration = 0
    centroid_array = initialCentroids(k)
    
    while iteration < 100:
        
        assignments = []
        
        """Assignment Step """
        for i in range(len(glucose_scaled)):
        
            glucose_value = glucose_scaled[i]
            hemoglobin_value = hemoglobin_scaled[i]
            distance_array = calculateDistanceArray(centroid_array, glucose_value, hemoglobin_value)
        
            min_index = np.argmin(distance_array)
            nearest_centroid = centroid_array[min_index][2]
    
            assignments.append([glucose_value, hemoglobin_value, nearest_centroid])
    
        assignment_array = np.array(assignments)
        new_classes = assignment_array[:,2]
        
        """ Update Step """
        for i in range(len(centroid_array)):
        
            centroid_array[i][0] = np.mean(assignment_array[new_classes==i][:,0])
            centroid_array[i][1] = np.mean(assignment_array[new_classes==i][:,1])
        
        iteration += 1
        
    print(centroid_array)
        
    return centroid_array, new_classes

def unscaledCentroids(centroid_array):
    
    c = []
    for i in range(len(centroid_array)):
        c1 = (centroid_array[i][0] * (490-70) + 70)
        c2 = (centroid_array[i][1] * (17.8-3.1) + 3.1)
        c3 = centroid_array[i][2]
        
        c.append([c1, c2, c3])
    
    unscaled_centroids = np.array(c)
    
    return unscaled_centroids

def graphingKMeans(glucose, hemoglobin, new_classes, unscaled_centroids):
    
    plt.figure()
    for i in range(int(new_classes.max())+1):
        rcolor = np.random.rand(3)
        plt.plot(hemoglobin[new_classes==i],glucose[new_classes==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(unscaled_centroids[i, 1], unscaled_centroids[i, 0], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("K Means Clustering Demo")
    plt.grid(True)
    plt
    plt.legend()
    plt.show()
    return
 
k = 3
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)
centroid_array, new_classes = kMeansClustering(k, glucose_scaled, hemoglobin_scaled)

unscaled_centroids = unscaledCentroids(centroid_array)
graphingKMeans(glucose, hemoglobin, new_classes, unscaled_centroids)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    