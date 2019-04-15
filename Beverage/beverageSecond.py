import pandas as matrix

import numpy as numerical

import matplotlib.pyplot as graphs

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from sklearn.cluster import KMeans

dataSet = matrix.read_csv("beverage_r.csv", sep = ";", index_col = 'numb.obs')

print(dataSet)

model = KMeans(n_clusters = 2, random_state = 42)

characteristic = model.fit(dataSet)

print(characteristic)

print("Array: ",model.labels_)

print("Array with (x;y): ", model.cluster_centers_)

K = range(1, 11)

models = [KMeans(n_clusters = k, random_state = 42).fit(dataSet) for k in K]

dist = [model.inertia_ for model in models]

graphs.plot(K, dist, marker='o')

graphs.xlabel('k')

graphs.ylabel('Sum of distances')

graphs.title('The Elbow Method showing the optimal number of classes')

graphs.show()

model = KMeans(n_clusters = 3, random_state = 42)

model.fit(dataSet)

dataSet['cluster'] = model.labels_

dataSet.groupby('cluster').mean()

print(dataSet.groupby('cluster').size())


