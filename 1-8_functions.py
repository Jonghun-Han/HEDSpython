#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

### A function takes some input and returns some output
# You can use built-in functions or create your own functions
# Overall, a function is just a piece of code that can be reused easily

# both def, the colon and the indentation are mandatory
def findFirstStringInCollection(collection, stringToFind):
    
    i = 0 
    while(collection[i] != stringToFind):
        i += 1 # another way to increment
    
    idFirstString = i
    
    return idFirstString # the return statement is mandatory to define outputs


collection1 = ['hurricane', 'earthquake', 'flood', 'hurricane']
stringToFind1 = 'flood'

collection2 = ['red', 'blue', 'yellow', 'green']
stringToFind2 = 'green'

collection3 = ['dog', 'cat', 'lion']
stringToFind3 = 'cat'


# with a single line (instead of the whole block above) you can perform the same task
id1 = findFirstStringInCollection(collection1, stringToFind1)
id2 = findFirstStringInCollection(collection2, stringToFind2)
id3 = findFirstStringInCollection(collection3, stringToFind3)
print(id1)
print(id2)
print(id3)

# The variables defined within the function are destroyed after running the function
# Only the returned variables will be kept
# Check the variable explorer: i is not defined. id1, id2, id3 are defined




### If we didn't use the function, the code above (6 lines) would have been:

# Uncomment and run to check it gives the same result as above
# i = 0 
# while(collection1[i] != stringToFind1):
#     i += 1 # another way to increment

# idFirstString = i
# print(idFirstString)

# i = 0 
# while(collection2[i] != stringToFind2):
#     i += 1 # another way to increment

# idFirstString = i
# print(idFirstString)

# i = 0 
# while(collection3[i] != stringToFind3):
#     i += 1 # another way to increment

# idFirstString = i
# print(idFirstString)
