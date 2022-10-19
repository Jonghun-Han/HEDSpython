#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# %% Functions

def calculateGini(X):
    # look in the "files" folder for the by-hand example
    
    # Calculate nominator
    nominator = 0
    for Xi in X:
        for Xj in X:
            nominator += abs(Xi - Xj)
    
    # Calculate denominator
    N = len(X)  
    Xbar = sum(X) / N    
    denominator = 2*N*(N-1)*Xbar
    
    # final calculation
    giniIndex = nominator / denominator
    
    return giniIndex


# %% Applications

myPopulation = [1200, 600, 5000]
gini = calculateGini(myPopulation)
print(gini)