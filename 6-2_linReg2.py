#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

"""
Supervised Learning - Linear Regression
@author: Aisha Aldosery
@module: Humanitarian Engineering and Data Science
"""

"""
Supervised Learning - Linear Regression
Problem: Find the realtinship between Max and Min temperature
"""

# Import Pacakges/Librarys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# uploading and Exploring dataset
filePath = 'files/weather.csv'
weather = pd.read_csv(filePath)
weather.head(10)
weather.describe()
# iterating the columns
for col in weather.columns:
    print('Columns Name:', col)
    
# Feature Selections:
    # 1. Maximum Temperature (MinTemp)
    # 2. Minimum Temperature (MaxTemp)
    
X = weather['MinTemp']
y = weather['MaxTemp']
# X.shape
# y.shape
# # Convert these two dataset from 1D array into 2D array using shape() function
X = X.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)
# X.shape
# y.shape

# Split the datasets into Training and Testing
 # 1. Training dataset (X_train, y_train) --> These datasets are used to fit the regression model
 # 2. Testing  dataset (X_test, y_test)   --> X.test is used to predict the dependent variable
                                            # while y_test is used to evaluate the confidence of the model 
                                                                               
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Create Regression Model
regressionModel = LinearRegression()
regressionModel.fit(X_train, y_train)

# Create Prediction
y_prediction = regressionModel.predict(X_test)

# Evaluate the model
confidence = regressionModel.score(X,y)
print('confidence', confidence)

# Plot the Regression Model
plt.figure(dpi=200)
plt.scatter(X_test, y_test, color='black', s=10)
plt.plot(X_test, regressionModel.predict(X_test), color='blue')
plt.title('MaxTemp VS MinTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()

# Plot predicted vs measured plot
plt.figure(dpi=200)
plt.scatter(y_test, regressionModel.predict(X_test), color='black', s=10)
plt.plot([-30, 50], [-30, 50], color='blue')
plt.xlabel('Measured')
plt.ylabel('Predicted')
plt.show()

#Example: what will be the maximum temp when the minumum temp =25
y_pred_25 = regressionModel.predict([[25]])
print(y_pred_25)