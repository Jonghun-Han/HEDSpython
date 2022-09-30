#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scientific Computation with Numpy
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Numpy is an open source Python library for scientific computing
# It is very useful for performing computations in data science
# (In terms of syntax, it works similarly to Matlab)

# when importing, you can use any name you want (this is valid for any library)
import numpy as np


# %% One-dimentional numpy arrays

x1 = np.array([15, 16, 17, 18, 19, 20]) # only integers
x2 = np.array([14.3, 0, 8.999]) # floats and integers
x3 = np.array([0, 2, 3])

# get the most important attributes of the array
print(x1.ndim) # number of axes, or dimentions
print(x1.shape) # the size of each dimention
print(x1.size) # the total number of elements in the array
print(x1.dtype) # the type of elements in the array

# %% different ways of creating arrays

a = np.array([1, 2, 3, 4])
b = np.array([(1.5, 2, 3), (4, 5, 6)])
c = np.array([[1, 2], [3, 4]], dtype=complex)
d = np.zeros((3, 4))
e = np.ones((2, 3))
f = np.arange(10, 30, 5)
g = np.arange(0.1, 2, 0.3)
h = np.linspace(1, 7, num=5) # Five equally-spaced numbers between 1 and 7

# %% access elements of the array (copy paste in the console)

x1[0] # the first element is called with a zero
x1[4] # the last element is located at the position len(x1)-1

x1[-1] # the last element can be also called with the index -1
x1[-2] # the index -2 refers to the second to last element, and so on

x1[:2] # access the first 2 elements
x1[-3:] # access the last 3 elements

x1[1:3] # access elements from index 1 to 3
x1[:2] # access every other element in the tuple

x1[::-1] # reversed x1

# %% Array operations

# multiply each component of the array by a number (scalar)
y1 = 3*x1 # we don't need a for loop. Compare with the code below

# yy1 = []
# for x in x1:
#     yy1.append(3*x)
# print(y1 == yy1)

# add/subtract a number to each component
3+x1
x2-5

# component by component array addition/subtraction (note: no for loop)
x2+x3
x3-x2
# x1-x3 # arrays must have the same dimention. Comment this line to proceed


# component by component array multiplication/division/power (note: no for loop)
x2*x3
x3/x2
x2**x3

# operations to modify existing array
x2 += 1 # add one to each element
x3 *= 2 # multiply each element by two


# Unary operations: mean, standard deviation, minimum, maximum, sum
# Those are implemented as methods of the ndarray class
# Note: unary means "having one operand"
print(x1.mean())
print(x1.std())
print(x1.min())
print(x1.max())
print(x1.sum())

# %% access built-in values and methods

print(np.pi) # value of pi
print(np.e) # value of e (neper number)

x4 = np.pi * np.array([0,0.5,1,1.5,2])

# %% Universal functions

y4 = np.sin(x4) # sin of numbers

# Look at these functions
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, 
# ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, 
# inner, invert, lexsort, max, maximum, mean, median, min, minimum, nonzero, 
# outer, prod, re, round, sort, std, sum, trace, 
# transpose, var, vdot, vectorize, where


# look at the documentation [highly recommended in this case]
# help(numpy)
# https://numpy.org/learn/