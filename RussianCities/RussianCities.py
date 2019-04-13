import pandas as matrix

import numpy as numerical

import matplotlib.pyplot as graphs

dataSet = matrix.read_csv("town_1959_2.csv", encoding = 'cp1251', index_col = u'номер')

print(dataSet)

print(dataSet.describe())

y = dataSet[u'население']

graphs.plot(y, 'r')

graphs.show()

newDataSet = dataSet.iloc[2 : 1004, :]

print(newDataSet.describe())

yNew = newDataSet[u'население']

graphs.plot(yNew, 'g')

graphs.show()

errorForDataWithMoscow = len(dataSet[dataSet['население'] < 52.925199]) / len(newDataSet) * 100

print("Error with Object Moscow: ",errorForDataWithMoscow)

errorForDataWithoutMoscow = len(dataSet[dataSet['население'] < 44.997904])/ len(dataSet) * 100

print("Error without Object Moscow: ",errorForDataWithoutMoscow)

medianValueWithoutMoscow = newDataSet.median()

print("Median result without Moscow: ", medianValueWithoutMoscow)

medianValueWithMoscow = dataSet.median()

print("Median result with Moscow: ", medianValueWithMoscow)

quartileValueWithoutMoscow = 37.550000 - 10.700000

print("Quartile method without Moscow: ", quartileValueWithoutMoscow)

quartileValueWithMoscow = 37.975000 - 10.700000

print("Quartile method with Moscow: ", quartileValueWithMoscow)

meanValueWithoutMoscow = newDataSet.mean()

print("Mean method without Moscow: ", meanValueWithoutMoscow)

meanValueWithMoscow = dataSet.mean()

print("Mean method with Moscow: ", meanValueWithMoscow)

meanValueOfIntermediateValues = (medianValueWithMoscow + medianValueWithoutMoscow +

                                 quartileValueWithMoscow + quartileValueWithoutMoscow +

                                 meanValueWithMoscow + meanValueWithoutMoscow) / 6

print("Predictive result: ", meanValueOfIntermediateValues)



