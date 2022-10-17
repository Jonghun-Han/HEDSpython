#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

### In Terminal
# conda install -n HEDSenv pip
# conda activate HEDSenv
# pip install wbdata
### End Terminal

### Double check in python console (in Spyder)
# import wbdata
# it should give no error
### End Double check

# https://blogs.worldbank.org/opendata/accessing-world-bank-data-apis-python-r-ruby-stata
# https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures

import wbdata
import pandas
import matplotlib.pyplot as plt

#set up the countries you want
countries = ["CL","UY","HU"]
# run "wbdata.get_country()" in python console for a list of countries

#set up the indicator you want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
# run "wbdata.get_indicator()" in python console for a list of indicators

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)

# a simple matplotlib plot with legend, labels and a title
dfu.plot(); 
plt.legend(loc='best'); 
plt.title("GNI Per Capita ($USD, Atlas Method)"); 
plt.xlabel('Date'); 
plt.ylabel('GNI Per Capita ($USD, Atlas Method');