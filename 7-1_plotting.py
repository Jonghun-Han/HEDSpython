#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# Examples of plotting
# Get more at: https://matplotlib.org/stable/plot_types/index.html

import matplotlib.pyplot as plt
import numpy as np

#%% General advise for plots

# Always generate the figure in high quality (dpi=200)
# Always add the labels on the axes
# Always add the units in square brackets
# if the variables are unitless, indicate [-]
# If there are many data series, add a legend (which means: add labels to data series)
# Place the legend such as it does not cover the plotted data
# Always provide good limits for the axes (xlim, ylim)

#%% Create Dummy data

x1 = np.linspace(0, 10, 100)
y1 = 4 + 2 * np.sin(2 * x1)
z1 = 1 + 4 * np.cos(2 * x1)

np.random.seed(3)
x2 = 0.5 + np.arange(8)
y2 = np.random.uniform(2, 7, len(x2))
z2 = 0.3*np.random.uniform(2, 7, len(x2))

np.random.seed(3)
x3 = 5 + np.random.normal(0, 2, 24)
y3 = 5 + np.random.normal(0, 2, len(x3))
x4 = 10 + np.random.normal(0, 2, 24)
y4 = 12 + np.random.normal(0, 2, len(x4))

np.random.seed(19680801)
n = 100
rng = np.random.default_rng()
x5 = rng.uniform(23, 32, n)
y5 = rng.uniform(0, 100, n)
z5 = rng.uniform(-50, -25, n)

np.random.seed(1)
x6 = 4 + np.random.normal(0, 1.5, 200)

#%% A bad line plot

fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.plot(x1, z1)
plt.show()

#%% A good line plot

fig, ax = plt.subplots(dpi=200)
ax.plot(x1, y1, linewidth=2.0, label='Sine fx')
ax.plot(x1, z1, linewidth=2.0, label='Cosine fx')
ax.set(xlim=(0, 10), xticks=np.arange(1, 11, 2),
       ylim=(-8, 8), yticks=np.arange(-8, 10, 2))
plt.grid(visible=None)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Height [cm]')
plt.show()

#%% Bar plot

fig, ax = plt.subplots(dpi=200)
ax.bar(x2, y2, linewidth=2.0)
ax.bar(x2, z2, linewidth=2.0)
ax.set(xticks=np.arange(1, len(x2)+1))
plt.grid(visible=None)
plt.xlabel('Day [-]')
plt.ylabel('Bananas [-]')
plt.show()

#%% Scatter plot

# note: you can use the size of the markers to represent another attribute
sizes = np.random.uniform(15, 80, len(x3)) 

fig, ax = plt.subplots(dpi=200)
ax.scatter(x3, y3, s=sizes, c='#d62728', vmin=0, vmax=100, label='poor HEDS')
ax.scatter(x4, y4, s=sizes, c='#2ca02c', vmin=0, vmax=100, label='good HEDS')
plt.xticks([], [])
plt.yticks([], [])
plt.grid(visible=None)
plt.xlabel('Humanitarian [-]')
plt.ylabel('Engineering [-]')
plt.legend(loc='lower right')
plt.show()

#%% 3D Scatter

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, dpi=200)
ax.scatter(x5, y5, z5)
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.xlabel('X [-]')
plt.ylabel('Y [-]')
ax.set_zlabel('Z [-]')
plt.show()

#%% Histogram

fig, ax = plt.subplots(dpi=200)
ax.hist(x6, bins=8, linewidth=0.5, edgecolor="white")
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))
plt.xlabel('Years of schooling [-]')
plt.ylabel('Occurrences [-]')
plt.grid(visible=None)
plt.show()

#%% Subplots

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5), dpi=200)
ax1.plot(x1, y1, 'o-')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Temperature [°]')
ax2.plot(x2, y2, '.-')
ax2.set_xlabel('time [s]')
ax1.set_ylim(1,7)
ax2.set_ylim(1,7)
ax1.grid(visible=None)
ax2.grid(visible=None)
plt.show()


