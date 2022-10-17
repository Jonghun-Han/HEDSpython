#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Types
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# API: Application Program Interface
# APIs allow two software to talk to each other

# REST (REpresentatational State Transfer) APIs
# allow communication between a client (your program) and a server (usually online)
# they use HTTP (HyperText Transfer Protocol) to communicate


# HTTP request sent from client to server. It contains the instructions in a file (usually .json)
# Server executes the instructions
# HTTP response from server to client. It contains the result


import requests
import json
import pandas

# define the HTTP request providing the appropriate URL
country = 'Italy'
daterange = '20211215-20220115'
url = ( 'https://covidmap.umd.edu/api/resources?indicator=covid&type=smoothed&country=' + 
    country + '&daterange=' + daterange )

# request data from API - collect the text response
response = requests.get(url).text

# transform the text response in a json file
jsonData = json.loads(response)

# convert json to pandas dataframe
df = pandas.DataFrame.from_dict(jsonData['data'])

