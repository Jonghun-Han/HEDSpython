#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Tuples are ordered sequences

tup1 = (5,1,6) # they are defined by round brackets. Commas are mandatory
tup2 = ('a', 'b', 'c', 'd') # they can contain elements of the same type
tup3 = (4, 'five and half', 6, 6.5, 'seven') # or different types
tup4 = ('lev1', 'lev1', ('lev2', 'lev2', 'lev2')) # Nesting: tuples can contain other tuples (or lists)


# access elements of a tuple (works like strings)
tup3[0] # the first element is called with a zero
tup3[4] # the last element is located at the position len(tup3)-1

tup3[-1] # the last element can be also called with the index -1
tup3[-2] # the index -2 refers to the second to last element, and so on

tup3[:2] # access the first 2 elements
tup3[-3:] # access the last 3 elements

tup3[1:3] # access elements from index 1 to 3
tup3[:2] # access every other element in the tuple

tup4[-1][2] # access the tuple at the end of tup4, and select its second element

# tuples are IMMUTABLE. Once created they can't be changed
# The next line will give an error. Try to uncomment it
# tup3[0] = 5

# if we want to manipulate tuples, we need to assign the result to another variable
tup1sorted = sorted(tup1) # note that the result is not a tuple anymore


# Lists are MUTABLE ordered lists
L1 = ['lev1', 'lev1', ('lev2', 'lev2', 'lev2')]
L2 = [4, 9, 0]
L3 = [5, 0, 11]

# once created, they can be modified
L1[1] = 'level 1'

# the next command is not allowed, because L1[2] is a tuple
# L1[2][0] = 5


# functions (or methods) for lists
L4 = L1 + L2 # concatenates

L2.append(1) # adds only ONE element at the end of L2
del(L2[1]) # deletes the second element 

L3.extend([4, 8]) # adds MANY elements at the end of L3


# why do we need immutable data types?
a = [1, 4, 7]
b = a # create an alias of a, named b
b[1] = 3 # change one element of b
print(a) # look that a has changed as well


# documentation
# help(tuple)
# help(list)