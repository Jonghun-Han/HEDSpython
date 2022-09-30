#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Dictionaries are a collection of keys and parameters
# They are defined by curly brackets
# The format is "KeyName":parameter. Commas are mandatory
person = {"Name": 'Napoleon', "Height": 1.45, "Weight": 60, "EmperorYears": [1804, 1815]} 


# access elements of a dictionary
print(person["Weight"])


# once created, they can be modified
person["Height"] = 5*0.3048 + 6*0.0254 # he was actually 5'6 


# methods applicable to dictionaries
person['horseColor'] = "White" # adds a key
print('Name' in person) # checks if the dictionary person has the key "Name"
print(person.keys()) # shows all the keys


# documentation
# help(dict)