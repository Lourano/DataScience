[Русский]
Пьятый проект по анализу данных.🤓
Задача классификации с помощью нейронной сети.
Постановка задачи: 
Определить поддельность швейцарского франка.
В качестве входных факторов выступают параметры купюры: длина, ширина и т.д. На выходном слое нейронная сеть выдает бинарный показатель 0 либо 1 (неподдельная  либо поддельная купюра).

[English]
Fifth data analysis project.🤓
Classification task using a neural network.
Formulation of the problem:
Determine the falsity of the Swiss franc.
The input parameters are bill parameters: length, width, etc. At the output layer, the neural network issues a binary indicator of 0 or 1 (a genuine or fake bill).


1.  Data Visualization

![myplot-5](https://user-images.githubusercontent.com/47052805/58955869-ac34b600-87a5-11e9-9a8f-62b2f5272f6f.png)

2.  Neural Network architecture 

![myplot2](https://user-images.githubusercontent.com/47052805/58955870-ad65e300-87a5-11e9-9fb8-7163d28a963e.png)

3.  First train. Activation function = sigmoid, in 3 layers. Accuracy = 51.13%

![firsttrain](https://user-images.githubusercontent.com/47052805/58956885-249c7680-87a8-11e9-8b67-fa755368bcf6.png)

4.  Second train. At input layer, function = relu. At hidden, output, function = sigmoid. Accuracy = 52.14%

![secondtrain](https://user-images.githubusercontent.com/47052805/58956891-29612a80-87a8-11e9-9551-8cff90cd07e2.png)

5.  Third train. At input, output layers, function = sigmoid. At hidden, function = softmax. Accuracy = 92.35%

![3train](https://user-images.githubusercontent.com/47052805/58956900-2f570b80-87a8-11e9-9957-a5a5882092cb.png)
