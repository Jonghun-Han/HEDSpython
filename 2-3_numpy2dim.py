#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two-dimentional Numpy
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

import numpy as np


# create arrays (two levels of square brackets are mandatory)
X1 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]]) # only integers
X2 = np.array([[14.3, 0.2, 8.999, 11], [3, 5, 1, 4]]) # floats and integers
X3 = np.array([[31, 32, 33], [21, 22, 23], [11, 12, 13]])
# have a look at the variable explorer

# visualise in matrix format
print(X1)
print(X2)

# shape and size
print(X2.shape) # gives the number of rows and columns
print(X2.size) # gives the number of elements


# access elements of the array (copy paste in the console)
X2[0] # first row
X2[1] # last row. Alternatively X2[-1]

X2[:,0] # first column
X2[:,2] # last column. Alternatively X2[:][-1]

# the first index corresponds to the row, the second to the column
X2[1,2] # access the element at the second row, third column
X2[0,-2:] # access the last 2 elements of the first row

# Note: the notation X2[1,2] is equivalent to X2[1][2]. Try it in the console


### Array operations

# multiply each component of the array by a number (scalar)
Y2 = 3*X2 # we don't need a for loop. Compare with the code below

# YY2 = []
# for i in [0, 1]:
#     YY2.append([])
#     for j in [0, 1, 2, 3]:
#         YY2[i].append(3*X2[i][j])
# print(Y2 == YY2)

# add/subtract a number to each component
3+X1
X2-5

# component by component array addition/subtraction (note: no for loop)
X1+X3 
X3-X1
# X1-X2 # arrays must have the same dimention. Comment this line to proceed


# component by component array multiplication/division/power (note: no for loop)
X1*X3
X1/X3
X3**X1


# mean, standard deviation, minimum, maximum, sum. They operate on the entire array
print(X1.mean())
print(X1.std())
print(X1.min())
print(X1.max())
print(X1.sum())

# mean of a single row (the same applies for the other methods)
X1[0].mean()


# numpy arrays can have an arbitrary number of dimentions
array3D = np.array([[[2,17], [45, 78]], [[88, 92], [60, 76]],[[76,33],[20,18]]])



# look at the documentation [highly recommended in this case]
# help(numpy)
# https://numpy.org/learn/