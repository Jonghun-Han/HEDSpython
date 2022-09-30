#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Manipulation and Visualisation
EMDAT_1900-2022_Earthquake_Flood_MassMovement_World
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""
# %% Define functions

def read_EMDAT(emdatXlsFilePath):
    rowsToSkip = range(6)
    rawData = pd.read_excel(emdatXlsFilePath, skiprows=rowsToSkip)
    return rawData

# def uniformPlot(plt):
#     plt.figure(dpi=200)
#     plt.rcParams['font.family'] = 'serif'
#     plt.rcParams['font.serif'] = 'Ubuntu'
#     plt.rcParams['font.monospace'] = 'Ubuntu Mono'
#     plt.rcParams['font.size'] = 18
#     plt.rcParams['axes.labelsize'] = 10
#     plt.rcParams['axes.labelweight'] = 'bold'
#     plt.rcParams['axes.titlesize'] = 10
#     plt.rcParams['xtick.labelsize'] = 8
#     plt.rcParams['ytick.labelsize'] = 8
#     plt.rcParams['legend.fontsize'] = 10
#     plt.rcParams['figure.titlesize'] = 12

# %% Import modules

import pandas as pd

from matplotlib import pyplot as plt
# pyplot provides a procedural interface to the matplotlib object-oriented 
# plotting library. It is modeled closely after Matlab. 
# Therefore, the majority of plotting commands in pyplot have Matlab analogs 
# with similar arguments

# %% Read EMDAT dataset

# EMDAT, world, 1900-2022, earthquakes, mass movements, floods
emdatFilePath = 'files/emdat_EQ_FL_LA_1900-2022_world.xlsx'
impactData = read_EMDAT(emdatFilePath)

# %% Pie chart: event types

hazTypesGeneral = pd.unique(impactData['Disaster Type'])

numHazTypeGeneral = []
splitYear = 1970
numHazTypeGeneralAfterYear = []
for hazType in hazTypesGeneral:
    numHazTypeGeneral.append(sum(impactData['Disaster Type'] == hazType))
    numHazTypeGeneralAfterYear.append(sum(impactData['Disaster Type'].eq(hazType) & \
                                          impactData['Start Year'].ge(splitYear)))

plt.figure(dpi=200)
plt.pie(numHazTypeGeneral, labels=hazTypesGeneral, autopct='%1.1f%%')

# plt.savefig('eventTypes.png', dpi=200) # this must be before plt.show()
plt.show()


# %% Pie chart: event types with year split

import numpy as np

hazToSplit = 2

# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=200)
fig.subplots_adjust(wspace=0)

# pie chart parameters
overall_ratios = numHazTypeGeneral
labels = hazTypesGeneral
explode = [0 for x in range(len(hazTypesGeneral))]
explode[hazToSplit] += 0.1

ax1.pie(overall_ratios, autopct='%1.1f%%', labels=labels, explode=explode)

# bar chart parameters
specific_ratios = [numHazTypeGeneral[hazToSplit]-numHazTypeGeneralAfterYear[hazToSplit], 
                   numHazTypeGeneral[hazToSplit]]
specific_labels = ['Before'+str(splitYear), str(splitYear)+' onwards']

width = 0.2
bc = ax2.bar(0, specific_ratios[0], width, bottom=None,
             label=specific_labels[0], color='C'+str(hazToSplit), alpha= 0.3)
ax2.bar_label(bc, labels=[f"{specific_ratios[0]}"], label_type='center')
bc = ax2.bar(0, specific_ratios[1], width, bottom=specific_ratios[0], 
             label=specific_labels[1], color='C2'+str(hazToSplit), alpha= 0.6)
ax2.bar_label(bc, labels=[f"{specific_ratios[1]}"], label_type='center')

ax2.set_title(hazTypesGeneral[hazToSplit])
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

plt.show()

# %% bar charts

minYear = min(impactData['Start Year'])
maxYear = max(impactData['Start Year'])

# all the events together
numEventsOneYear = []
for yr in range(minYear, maxYear+1):
    numEventsOneYear.append(sum(impactData['Start Year'] == yr))

plt.figure(dpi=200)
plt.bar(range(minYear, maxYear+1), numEventsOneYear)
plt.xlabel('Year')
plt.ylabel('Number of events [-]')
plt.show()

# disaggregated events
numEventsOneYearDisagg = dict()
for hazType in hazTypesGeneral:
    numEventsOneYearDisagg[hazType] = []
    for yr in range(minYear, maxYear+1):
        numEventsOneYearDisagg[hazType].append( 
            sum(impactData['Start Year'].eq(yr) & 
                impactData['Disaster Type'].eq(hazType) ) )

plt.figure(dpi=200)
prevSeries = None
for hazType in hazTypesGeneral:
    plt.bar(range(minYear, maxYear+1), numEventsOneYearDisagg[hazType], 
            label=hazType, bottom=prevSeries)
    prevSeries = numEventsOneYearDisagg[hazType]

plt.legend()
plt.xlabel('Year')
plt.ylabel('Number of events [-]')
plt.show()

# %% Clean lat/lon data

import re

for index, row in impactData.iterrows():
    
    try:
        # proper number or nan
        impactData['Longitude'][index] = float(impactData['Longitude'][index])
    except:
        # string
        impactData['Longitude'][index] = float(re.findall(
            r"[-+]?(?:\d*\.\d+|\d+)", impactData['Longitude'][index])[0])
    
    try:
        # proper number or nan
        impactData['Latitude'][index] = float(impactData['Latitude'][index])
    except:
        # string
        impactData['Latitude'][index] = float(re.findall(
            r"[-+]?(?:\d*\.\d+|\d+)", impactData['Latitude'][index])[0])

# %% Scatter plot with all events

plt.figure(dpi=200)

for ind,hazType in enumerate(hazTypesGeneral):
    impactSliced = impactData[impactData['Disaster Type'] == hazType]
    plt.scatter(impactSliced['Longitude'], impactSliced['Latitude'], 
                c='C'+str(ind), alpha=0.5, edgecolors='none', 
                label=hazType)

plt.legend()
plt.xlabel('Longitude [°]')
plt.ylabel('Latitude [°]')
plt.show()

# %% Scatter plot with single event types

plt.figure(dpi=200)

scaleFactor = [0.01, 10, 0.5]
for ind,hazType in enumerate(hazTypesGeneral):
    impactSliced = impactData[impactData['Disaster Type'] == hazType]
    plt.scatter(impactSliced['Longitude'], impactSliced['Latitude'], 
                c='C'+str(ind), alpha=0.5, edgecolors='none', 
                label=hazType, s=impactSliced['Total Deaths']*scaleFactor[ind])

    plt.title(hazType)
    plt.xlabel('Longitude [°]')
    plt.ylabel('Latitude [°]')
    plt.show()