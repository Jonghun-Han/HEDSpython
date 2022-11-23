#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Science Algorithms I: clustering, k-means, PCA
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

#%% Initial stuff
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
csvFilePath = 'files/WVS_Cross-National_Wave_7_csv_v4_0.csv'
rawData = pd.read_csv(csvFilePath)

#%% Check dataset and select only the desired features

print(['Initial shape of the dataset is', rawData.shape])

generalFeatures = ['B_COUNTRY_ALPHA', 'O1_LONGITUDE', 'O2_LATITUDE']
WVSgeneral = rawData.loc[:, generalFeatures]

Nquestions = 290
featuresToKeep = []
for q in range(1,Nquestions+1):
    featuresToKeep.append('Q'+str(q))

WVS = rawData.loc[:, featuresToKeep]

print(['Final shape of the dataset is', WVS.shape])

del rawData

#%% Histogram of countries

countries, numSurveysInCountry = np.unique(WVSgeneral.B_COUNTRY_ALPHA,return_counts=True)
dummy = range(len(countries))

plt.figure(dpi=200)
plt.bar(dummy,numSurveysInCountry, align='center')
plt.xticks(dummy, countries)
plt.xticks(rotation = 90)
plt.show()

#%% Clean dataset: fill blank spaces

# check most common answer to each question
nanQuestions = []
for q in range(1,Nquestions+1):
    labels, counts = np.unique(WVS['Q'+str(q)],return_counts=True)
    print( ['Q'+str(q)+':', 'Most common:', labels[counts.argmax()], 
            '#Empty:', WVS['Q'+str(q)].isna().sum()] )
    if np.isnan(labels[counts.argmax()]):
        nanQuestions.append(q)
    

# use the excel file and the questionnaire pdf to check "weird" values

# remove some of the questions
mostCommonIsNaN = ['Q92', 'Q223', 'Q230', 'Q240', 'Q266', 'Q267', 'Q268', 'Q276', 'Q280', 'Q282', 'Q290']
mostCommonIsWeird = ['Q272']
questionsToRemove = mostCommonIsNaN + mostCommonIsWeird
WVS = WVS.drop(questionsToRemove, axis=1)

# substitute NaNs with the most frequent answer for that question
for name, values in WVS.iteritems():
    labels, counts = np.unique(values,return_counts=True)
    values[values.isna()] = labels[counts.argmax()]
    
#%% Standardise the dataset onto unit scale (mean = 0 and variance = 1)

from sklearn.preprocessing import StandardScaler
standWVS = StandardScaler().fit_transform(WVS)

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#%% Sensitivity analysis for PCA

totVarianceExplained = []
NprincComp = range(2,100)
for comp in NprincComp:
    pcaObjDummy = PCA(n_components=comp)
    pcDummy = pcaObjDummy.fit_transform(standWVS)
    totVarianceExplained.append(sum(pcaObjDummy.explained_variance_ratio_))

plt.figure(dpi=200)
plt.plot(NprincComp, totVarianceExplained, marker='o')
plt.title('Sensitivity Analysis for PCA')
plt.xlabel('Number of PCs')
plt.ylabel('Total Explained Variance [-]')
plt.show()

#%% Two-component PCA

pcaObj = PCA(n_components=2)
prComp = pcaObj.fit_transform(standWVS)

plt.figure(dpi=200)
plt.scatter(prComp[:,0], prComp[:,1])
plt.xlabel('PC1 [-] VarExp=%1.2f' %pcaObj.explained_variance_ratio_[0])
plt.ylabel('PC2 [-] VarExp=%1.2f' %pcaObj.explained_variance_ratio_[1])
plt.show()

#%% Three-component PCA

pcaObj = PCA(n_components=3)
prComp = pcaObj.fit_transform(standWVS)

fig = plt.figure(1, figsize=(4, 3), dpi=200)
plt.clf()

ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
ax.set_position([0, 0, 0.95, 1])
plt.cla()
ax.scatter(prComp[:,0], prComp[:,1], prComp[:,2], cmap=plt.cm.nipy_spectral, edgecolor="k")
ax.set_xlabel('PC1 [-] VarExp=%1.2f' %pcaObj.explained_variance_ratio_[0])
ax.set_ylabel('PC2 [-] VarExp=%1.2f' %pcaObj.explained_variance_ratio_[1])
ax.set_zlabel('PC3 [-] VarExp=%1.2f' %pcaObj.explained_variance_ratio_[2])
plt.show()

#%% Elbow method for K-means

inertias = []
Nclusters = range(1,50)
for i in Nclusters:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(prComp)
    inertias.append(kmeans.inertia_)

plt.figure(dpi=200)
plt.plot(Nclusters, inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

#%% Final K-means

kmeans = KMeans(n_clusters=20)
kmeans.fit(prComp)

plt.figure(dpi=200)
plt.scatter(prComp[:,0], prComp[:,1], c= kmeans.labels_)
plt.xlabel('PC1 [-]')
plt.ylabel('PC2 [-]')
plt.show()


# try using the number of clusters equal to the number of nations in the survey
# then run K-means with that number of clusters
# then check if the natural division based on countries matches with k-means one

#%% Resources

# https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_3d.html
# https://scikit-learn.org/stable/modules/clustering.html#k-means
