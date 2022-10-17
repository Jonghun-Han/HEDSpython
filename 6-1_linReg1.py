# -*- coding: utf-8 -*-
"""
Supervised Learning - Linear Regression
@author: Aisha Aldosery
@module: Humanitarian Engineering and Data Science
"""

"""
Supervised Learning - Linear Regression
Step 1: Upload dataset 
Step 2: reshape your to ensure you have a 2D array
Step 3: Features Selection
Step 4: Split dataset into training and testing dataset
Step 5: Crete your model using the training set
Step 6: Make the prediction using testing set
Step 7: Calculate the confindence of your model
Step 8: Plot the regression
"""

# Import Pacakges/Librarys
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



# uploading and Exploring dataset
filePath = 'files/weatherHistory.csv'
weather = pd.read_csv(filePath)
weather.head(10)
weather.describe()

# Feature Selections:
    # 1. Summary (Summary)
    # 2. Humidity (Humidity)
    # 3. Temperature (Apparent Temperature (C))


temp = weather[["Humidity","Apparent Temperature (C)"]]
temp.head(12)

#2. Convert the categorical variable (Summary) into an indicator variables.
dummies = pd.get_dummies(weather["Summary"])
dummies.head(12)

#2. Concatinate the two temprary datasets temp1 and dummies.
X = pd.concat([temp,dummies],axis=1)
X.head(12)
# iterating the columns
for col in X.columns:
    print('Columns Name:', col)
    
# Split the datasets into Training and Testing
 # 1. Training dataset (X_train, y_train) --> These datasets are used to fit the regression model
 # 2. Testing  dataset (X_test, y_test)   --> X.test is used to predict the dependent variable
                                            # while y_test is used to evaluate the confidence of the model 

    

y = weather["Apparent Temperature (C)"]    # Predictin Y
X = X                                      # Independent X
# print(X.head(2))                                 

# Split the datasets into Training and Testing(30% for testing & 80% for training)
 # 1. Training dataset (X_train, y_train) --> These datasets are used to fit the regression model
 # 2. Testing  dataset (X_test, y_test)   --> X.test is used to predict the dependent variable
                                            # while y_test is used to evaluate the confidence of the mod

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# Create Regression Model
regressionModel = LinearRegression()
regressionModel.fit(X_train, y_train)

# Create Prediction
y_prediction= regressionModel.predict(X_test)
y_pred = y_prediction.reshape(1,-1)

# Evaluate the model
confidence = regressionModel.score(X,y)
print('confidence', confidence)

# Plot the Regression Model
plt.scatter(X_test["Humidity"], y_test, color='black')
plt.plot(X_test["Humidity"], y_prediction , color='blue')
plt.title('Temperature VS Humidity')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()

# Compare the actual and predicted valiues, both values are exactly the same 
result = pd.DataFrame(y_test)
result["y_predict"]= 0
result["y_predict"] = y_prediction
print(result.head(20))