#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Anything after an hashtag is a comment. The program won't read it

# Basic data types: integer, floating point (rational), string, boolean
a = 11
b = 123.4
c = 'Humanitarian' # quotes are needed. You can use both ' or "
d = True
# check the variable "explorer" panel


# Simple expressions on basic data types
A = 5 + 9
B = 5 - a # variables can be called in expressions
C = 4/2 # this is an int
D = a * b # this is a float
E = 4**2 # 4 to the power of 2
F = 4**-2 # 4 to the power of -2


# BEDMAS order: brackets, exponentials, divisions-multiplications, addition-subtraction
G1 = (a+B)*3
G2 = a+B*3 

# no result is normally printed on screen, unless the print function is called
print(G1)
print(G2)

# the function "=" assigns some data to a variable
# the function "==" checks if two variables are the same
result = G1==G2 # the variable result is a boolean
