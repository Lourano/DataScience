from nnv import NNV

import numpy as numerical

import pandas as matrix

from keras.models import Sequential

from keras.layers import Dense

import matplotlib.pyplot as figures

import seaborn as graphs

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

dataSet = matrix.read_csv("swiss_bank_notes.csv", index_col = False)

del dataSet['.']

labelEncoderForY = LabelEncoder()

dataSet['Status LE'] = labelEncoderForY.fit_transform(dataSet['Status'])

del dataSet['Status']

print(dataSet.head())

print(dataSet.info())

print(dataSet.describe())

print(dataSet.columns)

graphs.pairplot(dataSet)

figures.show()

DataX = dataSet.drop('Status LE', axis = 1)

DataY = dataSet['Status LE']

trainDataX, testAndValidationDataX, trainDataY, testAndValidationDataY = train_test_split(DataX, DataY, test_size = 0.3, random_state = 101)

validationDataX, testDataX, validationDataY, testDataY = train_test_split(testAndValidationDataX, testAndValidationDataY, test_size = 0.5, random_state = 101)

# neuralNetworkModel = Sequential()
#
# neuralNetworkModel.add(Dense(6, input_dim = 6, activation = 'relu'))
#
# neuralNetworkModel.add(Dense(4, activation = 'relu'))
#
# neuralNetworkModel.add(Dense(1, activation = 'sigmoid'))
#
# neuralNetworkModel.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
#
# fitModel = neuralNetworkModel.fit(trainDataX, trainDataY, epochs = 500, batch_size = 10, validation_data = (validationDataX, validationDataY))
#
# scores = neuralNetworkModel.evaluate(trainDataX, trainDataY)
#
# print("\n%s: %.2f%%" % (neuralNetworkModel.metrics_names[1], scores[1] * 100))

plotNeuralNetworkList = \
    [
        {"title": "", "units": 6, "color": "green"},

        {"title":"", "units": 4},

        {"title":"", "units": 1, "color" : "red"}

    ]

NNV(plotNeuralNetworkList, max_num_nodes_visible=20, node_radius=10, spacing_layer=60).render()

figures.plot(fitModel.history['loss'])

figures.plot(fitModel.history['val_loss'])

figures.title('Model loss')

figures.ylabel('Loss')

figures.xlabel('Epoch')

figures.legend(['Train', 'Val'], loc = 'upper right')

figures.show()














# figures.plot(fitModel.history['acc'])
#
# figures.plot(fitModel.history['val_acc'])
#
# figures.title('Model accuracy')
#
# figures.ylabel('Accuracy')
#
# figures.xlabel('Epoch')
#
# figures.legend(['Train', 'Val'], loc = 'lower right')
#
# figures.show()




























# dataSet = matrix.read_csv("swiss_bank_notes.csv", index_col = False)
#
# del dataSet['.']
#
# labelEncoderForY = LabelEncoder()
#
# dataSet['Status LE'] = labelEncoderForY.fit_transform(dataSet['Status'])
#
# del dataSet['Status']
#
# print(dataSet.head())
#
# print(dataSet.info())
#
# print(dataSet.describe())
#
# print(dataSet.columns)
#
# graphs.pairplot(dataSet)
#
# figures.show()
#
# DataX = dataSet.drop('Status LE', axis = 1)
#
# DataY = dataSet['Status LE']
#
# trainDataX, testDataX, trainDataY, testDataY = train_test_split(DataX, DataY, test_size = 0.3, random_state = 101)





























# logisticModel = LogisticRegression()
#
# logisticModel.fit(trainDataX, trainDataY)
#
# predictions = logisticModel.predict(testDataX)
#
# print(predictions)
#
# print(len(predictions))
#
# print(classification_report(testDataY ,predictions))
#
# print(logisticModel.score(testDataX, testDataY))




































































#
# print("Dimension: ",dataSet.shape)
#
# print("Rows: ", len(dataSet))
#
# print(dataSet.dtypes)
#
# print(dataSet.describe())
#
# dataSet['Length'].hist()
#
# graphs.show()
#
# dataSet.groupby('Status')['Length'].plot.hist(alpha = 0.6)
#
# graphs.legend()
#
# graphs.show()
#
# colors = {'genuine' : 'green', 'counterfeit' : 'red'}
#
# scatter_matrix(dataSet, figsize = (6, 6), diagonal = 'kde', c = dataSet['Status'].replace(colors), alpha = 0.2)
#
# graphs.show()
#
# dataSet.groupby('Status')['Diagonal'].plot.hist(alpha = 0.6)
#
# graphs.legend(loc = 'upper left')
#
# graphs.show()
#
# dataSet.plot.scatter(x = 'Top', y = 'Bottom', c = dataSet['Status'].replace(colors))
#
# graphs.show()









