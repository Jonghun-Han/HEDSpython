#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""


# an absolute path for a file starts from the root of the hard drive (C:/ or Users)
absoluteFilePath = '/Users/roberto/2021 humanitarian data science/HEDS python/files/humEng.txt'


# a relative file path starts from the working directory (HEDS python in this case)
relativeFilePath = 'files/humEng.txt'

# type the command "pwd" in the console to check which one is your working directory
# note: pwd stands for "path to working directory"



# open the file in the read mode "r"
#fileHandle = open(absoluteFilePath, 'r')
# this line will give error, since the indicated absolute path does not exist in your computer
# comment this command to proceed


# relative paths work in every computer, as long as the pwd is right
fileHandle = open(relativeFilePath, 'r')

# use the readline method to read a line of the file
line1 = fileHandle.readline()
line2 = fileHandle.readline()
line3 = fileHandle.readline()
line4 = fileHandle.readline()

# always close the file after reading/writing stuff in it
fileHandle.close()

# this command will give error because the file is closed
# fileHandle.readline()


# have a look at the documentation

# import io
# help(io.TextIOBase)