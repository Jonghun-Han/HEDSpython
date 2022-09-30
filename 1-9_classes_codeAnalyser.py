#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Not necessarily needed for Humanitarian Engineering and Data Science

# abstract superclass (works for any shape)
class shape():
    def getArea(self):
        pass
    
# concrete class 1 (a specific object)
class circle(shape):
    def __init__(self, radius):
        self.shape = 'circle'
        self.radius = radius
        self.area = None
        
    def getArea(self):
        self.area = 3.14*self.radius**2

# concrete class 2 (a specific object)
class rectangle(shape):
    def __init__(self, base, height):
        self.shape = 'rectangle'
        self.base = base
        self.height = height
        self.area = None
        
    def getArea(self):
        self.area = self.base * self.height
        
a = circle(1)
a.getArea()
print(a.area)

b = rectangle(1,2)
b.getArea()
print(b.area)