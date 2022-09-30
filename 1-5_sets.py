#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Sets are collections without duplicates
# They are defined with curly brackets. Commas are mandatory
hazardsModel1 = {'Flood', 'Earthquake', 'Hurricane', 'Pandemics'}
hazardsModel2 = {'Earthquake', 'Pandemics'}

# lists can have duplicates, sets cannot
dummyList = ['Earthquake', 4, 8, 'Pandemics', 'Pandemics']
dummySet = {'Earthquake', 4, 8, 8, 'Hurricane', 'Pandemics', 'Pandemics'}

print(dummyList)
print(dummySet)

# duplicate elements (of string type) are defined considering the case
print({'Earthquake', 4, 8, 8, 'Hurricane', 'pandemics', 'Pandemics'})

# methods applicable to sets
intersection = hazardsModel1 and hazardsModel2 # intersection. 
union = hazardsModel1 or hazardsModel2 # union of two sets
union2 = hazardsModel1.union(hazardsModel2) # alternative way to perform union

# copy paste in the console: union.add(5)
# adds en element to the union set
# Sets are mutable: what happened to the hazardModel1 set? [side effect]


# check if an element is in a set
print("Hurricane" in hazardsModel1)
print("Hurricane" in hazardsModel2)

# documentation
# help(set)