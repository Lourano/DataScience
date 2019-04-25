import numpy as numerical

import pandas as matrix

import matplotlib.pyplot as figures

import seaborn as graphs

from sklearn.model_selection import train_test_split

from scipy.stats.mstats import zscore

from sklearn.linear_model import LinearRegression

from sklearn import metrics

import statsmodels.api as statistic

from scipy import stats

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

from gmdhpy.gmdh import MultilayerGMDH

USAHousing = matrix.read_csv("USA_Housing.csv")

print(USAHousing.head())

print(USAHousing.info())

print(USAHousing.describe())

print(USAHousing.columns)

graphs.heatmap(USAHousing.corr(),annot = True)

figures.title('Correlation')

figures.savefig('corr.png')

figures.show()

figures.figure(figsize = (20, 12))

figures.scatter(USAHousing['Avg. Area Number of Rooms'], USAHousing['Price'])

figures.show()

figures.figure(figsize = (20, 12))

figures.scatter(USAHousing['Avg. Area Number of Bedrooms'], USAHousing['Price'])

figures.show()

graphs.pairplot(USAHousing)

figures.title('Visualization')

figures.savefig('vis.png')

figures.show()

graphs.distplot(USAHousing['Price'])

figures.show()

dataX = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']]

dataY = USAHousing['Price']

normalizedDataY = matrix.Series(zscore(dataY), index = dataY.index)

normalizedDataX = matrix.DataFrame(data = zscore(dataX), index = dataX.index, columns = dataX.columns)

trainDataX, testDataX, trainDataY, testDataY = train_test_split(normalizedDataX, normalizedDataY, test_size = 0.4, random_state = 101)


############ PART 1. LINEAR REGRESSION ############


linearModel = LinearRegression()

linearModel.fit(trainDataX, trainDataY)

print(linearModel.intercept_)

coefficients = matrix.DataFrame(linearModel.coef_, dataX.columns, columns = ['Coefficients'])

print(coefficients)

predictionByLinearRegression = linearModel.predict(testDataX)

figures.scatter(testDataY, predictionByLinearRegression)

figures.title('Linear Model')

figures.savefig('linear.png')

figures.show()

print('MAE by Linear Regression: ', metrics.mean_absolute_error(testDataY, predictionByLinearRegression))

print('MSE by Linear Regression: ', metrics.mean_squared_error(testDataY, predictionByLinearRegression))

print('RMSE by Linear Regression: ', numerical.sqrt(metrics.mean_squared_error(testDataY, predictionByLinearRegression)))

variableForStatisticX = statistic.add_constant(trainDataX)

print(variableForStatisticX.head())

variableForEST = statistic.OLS(trainDataY, variableForStatisticX)

variableForESTVisualization = variableForEST.fit()

print(variableForESTVisualization.summary())

VIFS = [vif(variableForStatisticX.values, i) for i in range(len(variableForStatisticX.columns))]

matrix.Series(data = VIFS, index = variableForStatisticX.columns)

############ PART 2. GMDH FOR REGRESSION ANALYSIS ############

GMDH = MultilayerGMDH(ref_functions = 'linear')

GMDHModel = GMDH.fit(trainDataX, trainDataY)

predictionByGMDH = GMDH.predict(testDataX)

figures.scatter(testDataY, predictionByGMDH)

figures.title('GMDH Model')

figures.savefig('GMDH.png')

figures.show()

print('MAE by GMDH: ', metrics.mean_absolute_error(testDataY, predictionByGMDH))

print('MSE by GMDH: ', metrics.mean_squared_error(testDataY, predictionByGMDH))

print('RMSE by GMDH: ', numerical.sqrt(metrics.mean_squared_error(testDataY, predictionByGMDH)))

RSquaredForGMDBMethod = metrics.r2_score(testDataY, predictionByGMDH)

print('R^2 By GMDH: ', RSquaredForGMDBMethod)

figures.scatter(testDataY, predictionByLinearRegression, color = 'red', label = 'Regression Model')

figures.scatter(testDataY, predictionByGMDH, color = 'blue', alpha = 0.3, label = 'GDMH Model')

figures.legend()

figures.title('Comparison of Models')

figures.savefig('comp.png')

figures.show()


















