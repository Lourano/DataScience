import pandas as matrix

import numpy as numerical

import matplotlib.pyplot as graphs

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

dataSet = matrix.read_csv("beverage_r.csv", sep = ";", index_col = 'numb.obs')

print(dataSet)

link = linkage(dataSet, 'ward', 'euclidean')

print(link[:5])

dn = dendrogram(link, orientation = "right")

graphs.show()

dataSet['cluster'] = fcluster(link, 4, criterion = "distance")

clusterShow = dataSet.groupby('cluster').mean()

print(clusterShow)

clusterization =  dataSet.groupby('cluster').size()

print(clusterization)


