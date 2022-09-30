#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Comparison operators compare some values and return a Boolean (true/false) as a result
a = 6

# copy paste in the console
a == 6 # equality
a == 1

a != 6 # inequality
a != 1 

a > 2
a >= 7

a < 2
a <= 10


# if statement
# do something if a condition is met, do something else instead

age1 = 20
age2 = 16

# note that the colon is mandatory
# note that the indentation is mandatory
if age1 >= 18:
    print('The first person can enter a pub')
else:
    print('The first person cannot enter a pub')
    
if (age2 >= 18): # brackets are not mandatory
    print('The second person can enter a pub')
else:
    print('The second person cannot enter a pub')