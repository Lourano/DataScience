import pandas as matrix

import numpy as numerical

import matplotlib

import matplotlib.pyplot as graphs

from scipy.stats.kde import gaussian_kde

from numpy import linspace, hstack

from pylab import plot, show, hist

dataSet = matrix.read_csv("AmesHousing.txt", sep = "\t", header = 0, index_col = False)

print(dataSet.head())

print(dataSet.dtypes)

print(dataSet.describe(include = 'all'))

graphs.hist(dataSet['SalePrice'], bins = 60)

graphs.title("Histogram of Sales")

show()

numerical.log(dataSet['SalePrice']).hist(bins = 45)

graphs.title("Prologarithmed Histogram of Sales")

show()

# density = gaussian_kde(dataSet['SalePrice'])

# density = gaussian_kde(dataSet['SalePrice'], bw_method = 5)

# density = gaussian_kde(dataSet['SalePrice'], bw_method = 1)

density = gaussian_kde(dataSet['SalePrice'], bw_method = 0.1)

x = linspace(min(dataSet['SalePrice']), max(dataSet['SalePrice']), 1000)

plot(x, density(x), 'g')

hist(dataSet['SalePrice'], density = 1, alpha = .3)

graphs.title("Histogram of Sales with Plot of Gaussian KDE")

show()

plot(x, density(x), 'r')

graphs.title("Plot of Gaussian KDE")

show()

dataSet.groupby('MS Zoning')['SalePrice'].plot.hist(density = 1, alpha = 0.6)

graphs.legend()

graphs.title("Histogram of Comparison through  MS Zoning with SalePrice")

show()

boxPlot = dataSet.boxplot(column = 'SalePrice', by = 'MS Zoning')

boxPlot.get_figure().suptitle('')

graphs.title("Box Plot of Comparison through  MS Zoning with SalePrice")

show()

print(dataSet['MS Zoning'].value_counts())




