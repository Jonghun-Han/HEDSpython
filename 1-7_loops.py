#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

### For Loops perform a task for a specific number of times

# Define a list
xValues = [15, 16, 17, 18, 19, 20]

# colon is mandatory to define the for loop
for x in xValues: # everything that's indented will be considered in the loop
    print(x)


# example: represent the function y = 3x for a set of x values
yValues = [] # define an empty list that will contain the values of y

for x in xValues:
    yValues.append(3 * x)
    
print(yValues) # this is the first command which is not in the loop


# for loops can iterate over non-numerical lists/tuples as well
disasters = ('hurricane', 'earthquake', 'flood', 'hurricane')

# the function enumerate gives you both the index and the content of a list/tuple
for index,disaster in enumerate(disasters): 
    print([index, disaster])
    
    
### While loops repeat a set of code until a condition is met

i = 0 # define starting index (to evaluate a condition)
while(disasters[i] != 'flood'):
    i = i + 1 # increment i if the condition is met (skip that element of the tuple/list)

print('The first element of the tuple containing a flood is')    
print([i, disasters[i]])