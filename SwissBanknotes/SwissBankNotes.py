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

neuralNetworkModel = Sequential()

neuralNetworkModel.add(Dense(6, input_dim = 6, activation = 'sigmoid'))

neuralNetworkModel.add(Dense(8, activation = 'softmax'))

neuralNetworkModel.add(Dense(1, activation = 'sigmoid'))

neuralNetworkModel.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

fitModel = neuralNetworkModel.fit(trainDataX, trainDataY, epochs = 250, batch_size = 10, validation_data = (validationDataX, validationDataY))

scores = neuralNetworkModel.evaluate(trainDataX, trainDataY)

print("\n%s: %.2f%%" % (neuralNetworkModel.metrics_names[1], scores[1] * 100))

plotNeuralNetworkList = \
    [
        {"title": "", "units": 6, "color": "green"},

        {"title":"", "units": 8},

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
