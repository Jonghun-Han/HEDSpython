#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Pandas is an open source Python library for data analysis
# A library allows to add more functions (methods) to the basic Python

# Most of the times it is pre-installed in your system, but you need to import it

# this statement allows to import all the methods in the pandas library
# every pandas-related method will be called as pandas.nameOfTheMethod
import pandas

# https://data.humdata.org/dataset/idmc-internally-displaced-persons-idps-new-displacement-associated-with-disasters
csvFilePath = 'files/internallyDisplaced.csv'

# the read_csv method allows you to import the csv as a DataFrame variable
# the first line of the csv will give name to the columns of the dataframe
internallyDisplaced = pandas.read_csv(csvFilePath)
# check the variable explorer, double click on this variable

# you can also read excel files with the "read_excel" method. The rest is the same
# internallyDisplaced = pandas.read_excel(xlsFilePath)
# warning: define xlsFilePath to run this command


### Manipulate dataframes

# create new dataframes with portions of the original one ()
newDataFrame = internallyDisplaced['Year'] # one field only
newDataFrame = internallyDisplaced.Year # Equivalent to the line above
newDataFrame2 = internallyDisplaced[['Year', 'New Displacements']] # more fields (in a list)

# access specific elements
print(internallyDisplaced.Year[0])
print(internallyDisplaced['Hazard Type'][0]) # both the dot and the brackets are valid

# create a new dataframe only considering events happened after 2014
afterGivenYear = internallyDisplaced['Year'] >= 2014 # boolean for each row
internallyDisplacedAfterGivenYear = internallyDisplaced[afterGivenYear] # select only the rows with a "True" value in the variable above
# can you merge these two lines in a single line?

# save the new dataframe to a csv file
internallyDisplacedAfterGivenYear.to_csv('files/internallyDisplacedAfter2014.csv')
# note: the file is saved in the working directory. Try uncommenting the command below
#internallyDisplacedAfterGivenYear.to_csv('files/internallyDisplacedAfter2014.csv')


# identify the unique types within a column
whichHazards = internallyDisplaced['Hazard Type'].unique()
# are you able to save a dataframe containing only flood events?



# look at the documentation [highly recommended in this case]
# help(pandas)
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html