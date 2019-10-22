import pandas as matrix

import numpy as numerical

import matplotlib.pyplot as figures

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from sklearn.cluster import KMeans

from sklearn.model_selection import train_test_split

from scipy.spatial.distance import cdist

from scipy.stats.mstats import zscore

from sklearn.decomposition import PCA

import seaborn as graphs

dataSet = matrix.read_csv("USA_Housing.csv")

del dataSet['Address']

print(dataSet)

normalizedDataSet = matrix.DataFrame(data = zscore(dataSet), index = dataSet.index, columns = dataSet.columns)

trainData, testData = train_test_split(normalizedDataSet,  test_size = 0.01, random_state = 123)

numberOfClusters = range(1, 10)

meanDistance = []

for k in numberOfClusters:

    clusterModel = KMeans(n_clusters = k)

    clusterModel.fit(trainData)

    clusterAssign = clusterModel.predict(trainData)

    meanDistance.append(sum(numerical.min(cdist(trainData, clusterModel.cluster_centers_, 'euclidean'), axis = 1))

     / trainData.shape[0])


figures.plot(numberOfClusters, meanDistance)

graphs.dark_palette('blue')

figures.xlabel('Number of Clusters')

figures.ylabel('Distances')

figures.show()

clusterModelByElbow = KMeans(n_clusters = 3)

clusterModelByElbow.fit(trainData)

clusterAssignByElbow = clusterModelByElbow.predict(trainData)

variableForPCA = PCA(2)

arrayForPlotting = variableForPCA.fit_transform(trainData)

figures.scatter(arrayForPlotting[:, 0], arrayForPlotting[:, 1], c = clusterModelByElbow.labels_)

graphs.dark_palette('blue')

figures.show()

trainData.reset_index(level = 0, inplace = True)

clusterList = list(trainData['index'])

clusterLabels = list(clusterModelByElbow.labels_)

newClusterList = dict(zip(clusterList, clusterLabels))

newCluster = matrix.DataFrame.from_dict(newClusterList, orient = 'index')

newCluster.columns = ['Cluster']

newCluster.reset_index(level = 0, inplace = True)

newDataSetWithCluster = matrix.merge(trainData, newCluster, on = 'index')

print("Data With index of Clusters:")

print("\n", newDataSetWithCluster)

sortedDataSetWithCluster = newDataSetWithCluster.sort_values(by = ['Cluster'], axis = 0)

sortedDataSetWithClusterWithNormIndex = matrix.read_csv("sortedDataSetWithCluster.csv", index_col = False)

del sortedDataSetWithClusterWithNormIndex['Unnamed: 0']

del sortedDataSetWithClusterWithNormIndex['index']

print("\n Sorted Data Set With Index\n",sortedDataSetWithClusterWithNormIndex)

LogicVariableForFilterForZeroCluster = sortedDataSetWithClusterWithNormIndex['Cluster'] == 0

LogicVariableForFilterForFirstCluster = sortedDataSetWithClusterWithNormIndex['Cluster'] == 1

LogicVariableForFilterForSecondCluster = sortedDataSetWithClusterWithNormIndex['Cluster'] == 2

NewDataSetWithZeroCluster = sortedDataSetWithClusterWithNormIndex[LogicVariableForFilterForZeroCluster]

NewDataSetWithFirstCluster = sortedDataSetWithClusterWithNormIndex[LogicVariableForFilterForFirstCluster]

NewDataSetWithSecondCluster = sortedDataSetWithClusterWithNormIndex[LogicVariableForFilterForSecondCluster]


NewDataSetWithZeroClusterWithFactorX1 = NewDataSetWithZeroCluster['Avg. Area Income']

NewDataSetWithZeroClusterWithFactorX2 = NewDataSetWithZeroCluster['Avg. Area House Age']

NewDataSetWithZeroClusterWithFactorX3 = NewDataSetWithZeroCluster['Avg. Area Number of Rooms']

NewDataSetWithZeroClusterWithFactorX4 = NewDataSetWithZeroCluster['Area Population']


NewDataSetWithFirstClusterWithFactorX1 = NewDataSetWithFirstCluster['Avg. Area Income']

NewDataSetWithFirstClusterWithFactorX2 = NewDataSetWithFirstCluster['Avg. Area House Age']

NewDataSetWithFirstClusterWithFactorX3 = NewDataSetWithFirstCluster['Avg. Area Number of Rooms']

NewDataSetWithFirstClusterWithFactorX4 = NewDataSetWithFirstCluster['Area Population']


NewDataSetWithSecondClusterWithFactorX1 = NewDataSetWithSecondCluster['Avg. Area Income']

NewDataSetWithSecondClusterWithFactorX2 = NewDataSetWithSecondCluster['Avg. Area House Age']

NewDataSetWithSecondClusterWithFactorX3 = NewDataSetWithSecondCluster['Avg. Area Number of Rooms']

NewDataSetWithSecondClusterWithFactorX4 = NewDataSetWithSecondCluster['Area Population']


def functionForGinniIndex(data):

    count = data.size

    coefficient = 2 / count

    indexes = numerical.arange(1, count + 1)

    weighted_sum = (indexes * data).sum()

    total = data.sum()

    constant = (count + 1) / count

    return coefficient * weighted_sum / total - constant


print("\nImpurity function for cluster (0) by  Avg. Area Income (X1): ", functionForGinniIndex(NewDataSetWithZeroClusterWithFactorX1))

print("\nImpurity function for cluster (0) by  Avg. Area House Age (X2):", functionForGinniIndex(NewDataSetWithZeroClusterWithFactorX2))

print("\nImpurity function for cluster (0) by  Avg. Area House Age (X3):", functionForGinniIndex(NewDataSetWithZeroClusterWithFactorX3))

print("\nImpurity function for cluster (0) by  Avg. Area House Age (X4):", functionForGinniIndex(NewDataSetWithZeroClusterWithFactorX4))


print("\nImpurity function for cluster (1) by  Avg. Area House Age (X1):", functionForGinniIndex(NewDataSetWithFirstClusterWithFactorX1))

print("\nImpurity function for cluster (1) by  Avg. Area House Age (X2):", functionForGinniIndex(NewDataSetWithFirstClusterWithFactorX2))

print("\nImpurity function for cluster (1) by  Avg. Area House Age (X3):", functionForGinniIndex(NewDataSetWithFirstClusterWithFactorX3))

print("\nImpurity function for cluster (1) by  Avg. Area House Age (X4):", functionForGinniIndex(NewDataSetWithFirstClusterWithFactorX4))


print("\nImpurity function for cluster (2) by  Avg. Area House Age (X1):", functionForGinniIndex(NewDataSetWithSecondClusterWithFactorX1))

print("\nImpurity function for cluster (2) by  Avg. Area House Age (X2):", functionForGinniIndex(NewDataSetWithSecondClusterWithFactorX2))

print("\nImpurity function for cluster (2) by  Avg. Area House Age (X3):", functionForGinniIndex(NewDataSetWithSecondClusterWithFactorX3))

print("\nImpurity function for cluster (2) by  Avg. Area House Age (X4):", functionForGinniIndex(NewDataSetWithSecondClusterWithFactorX4))
