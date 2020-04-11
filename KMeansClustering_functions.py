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
        
        rand = random.randint(0, len(glucose))
        g = (glucose[rand]-70)/(490-70)
        h = (hemoglobin[rand]-3.1)/(17.8-3.1)
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
    #print(distance_array)
    
    return distance_array

def kMeansClustering(k, glucose_scaled, hemoglobin_scaled):
    
    centroid_array = initialCentroids(k)
    
    assignments = []
    iteration = 0
    
    while iteration < 100:
   
        """Assignment Step """
        for i in range(len(glucose_scaled)):
        
            glucose_value = glucose_scaled[i]
            hemoglobin_value = hemoglobin_scaled[i]
            distance_array = calculateDistanceArray(centroid_array, glucose_value, hemoglobin_value)
        
            min_index = np.argmin(distance_array)
            nearest_centroid = centroid_array[min_index][2]
        
            classification = [glucose_value, hemoglobin_value, nearest_centroid]
            assignments.append(classification)
    
        assignment_array = np.array(assignments)
        classification = assignment_array[:,2]
        
        """ Update Step """
        for i in range(len(centroid_array)):
        
            centroid_array[i][:2] = np.mean(assignment_array[classification==i])
        
        iteration += 1
    



k = 3
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled, classification = normalizeData(glucose, hemoglobin, classification)

centroid_array = initialCentroids(k)

kMeansClustering(k, glucose_scaled, hemoglobin_scaled)

    

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    