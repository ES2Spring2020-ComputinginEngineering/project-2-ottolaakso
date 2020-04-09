""" Step 4 Code """
""" Otto Laakso """

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification
