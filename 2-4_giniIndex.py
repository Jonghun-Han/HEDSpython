#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# %% Functions

def get_gini(array):
    """Calculate the Gini coefficient of a 1D numpy array."""
    # http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    
    array += np.spacing(1) # Values cannot be 0: add a microscopical value
    array = np.sort(array) # Values must be sorted
    index = np.arange(1, array.shape[0]+1) # Index per array element
    n = array.shape[0] # Number of array elements:
    
    giniIndex = ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))
    return giniIndex

# %% Applications

import numpy as np
from matplotlib import pyplot as plt

Npoints = 500000

# %% Compute for one population

pop = np.ones([Npoints,1])
gini1 = get_gini(pop)

plt.figure(dpi=200)
plt.hist(pop, bins=20)
plt.xlabel("Income [-]")
plt.ylabel("Number of people [-]")
plt.title("Gini: %.4f" %(gini1))
plt.show()

# %% Compute for different populations and compare

populations = {
    'Flat': 5*np.ones([int(Npoints/3),1]),
    'Uniform': np.random.rand(Npoints),
    'Normal': np.random.normal(loc=5, scale=2, size=Npoints),
    'Exponential': np.random.exponential(scale=1, size=Npoints),
    'Gamma': np.random.gamma(2, 2, Npoints),
    'Beta': np.random.beta(0.5, 0.5, Npoints),
    }

plt.figure(dpi=200)
for pop in populations:
    gini = get_gini(populations[pop])
    plt.hist(populations[pop], bins=20, label="%s: %.4f" %(pop,gini), 
             alpha=0.4)
    
plt.legend()
plt.xlabel("Income [-]")
plt.ylabel("Number of people [-]")
plt.show()

# %% Use GDP of countries and calculate the Gini index