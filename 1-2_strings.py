#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

s1 = 'Humanitarian'
s2 = 'Engineering'
s3 = 'and'
s4 = "Data" 
s5 = 'Science' # quotes are needed to define strings. You can use both ' or "

# Concatenation of strings (+)
humEng = s1 + s2
humDataScience = s1 + s4 + s5
humEngDataScience = humEng + s3 + s4 + s5 + 'is the best'
# note that subtraction, multiplication, division, etc. are not defined between strings

print(humEng)
print(humDataScience)
print(humEngDataScience)
# note that there are no spaces (try to redefine s1 to s5 to add the spaces)

# replicate a string 3 times
print(3*s1)

# length command
print(len(humEng)) # check how many characters compose the string humEng

# access parts of a string (copy paste these commands in the console)
humEng[0] # the first character in a string is called with a zero

humEng[22] # the last character is located at the position len(string)-1
humEng[-1] # the last character can be also called with the index -1
humEng[-2] # the index -2 refers to the second to last character, and so on

humEng[:5] # access the first 5 characters
humEng[-4:] # access the last 4 characters

humEng[9:15] # access characters from index 9 to 15
humEng[9:15:2] # access every other character from index 9 to 15


# Example function (or method) to apply on strings
lowerCase = humDataScience.lower() 
print(lowerCase)

# the method "lower" does not require parameters to run, so the brackets are empty

help(str) # check the other available methods
