"""
Reference:
https://medium.com/@waadlingaadil/learn-to-build-a-neural-network-from-scratch-yes-really-cac4ca457efc
https://www.geeksforgeeks.org/backpropagation-in-neural-network/
Course Textbook - Business Intelligence, Analytics, Data Science, and AI

Objectives
1) An input layer that takes input data as a matrix receives and passes it on
2) A hidden layer
3) An output layer
4) Weights and biases between the layers
5) Multiply the input by a set of weights (via matrix multiplication)
6) Apply deliberate activation function for every hidden layer
7) Return an output
8) Calculate error by taking the difference from the desired output and the predicted output, giving us the gradient descent to provide our loss function
9) Apply loss function to weights
10) Repeat this process no less than 1,000 times to train the ANN
"""

import numpy as np
import random

def activation_function(x):
    """
    activation_function applies the liner activation function

    :param x: input data 
    """
    return x

def activation_derivative(x):
    """
    activation_function applies the derivative of the liner 
    activation function

    :param x: input data 
    """
    return 1

def normalize_dataset(data):
    """
    normalize_dataset normalizes the data by converting 
    it into a unit vector between 0 and 1, which helps the
    model converge during gradient descent

    :param data: input data to be normalized
    """
    ret = []
    for set in data:
        min_vals = np.min(set, axis=0)
        max_vals = np.max(set, axis=0)
        ranges = max_vals - min_vals
        normalized_set = (set - min_vals) / ranges
        ret.append(normalized_set)
    return np.array(ret)

def generate_average_data_sample(length):
    """
    generate_average_data generates synthetic testing data.
    The data contains 'length' features randomly generated
    between a randomly generated min and max value

    :param length:      the number of features in each sample
    """
    ret = []
    max = random.randint(10, 100)
    min = random.randint(0, max-10)
    for x in range(length):
        ret.append(random.randint(min, max))
    ret.append(sum(ret)/len(ret))
    return ret

def generate_average_data(num_samples, length):
    """
    generate_average_data generates synthetic testing data.
    The data contains 'length' features randomly generated
    between a randomly generated min and max value

    :param num_sample:  the number of samples
    :param length:      the number of features in each sample
    """
    data_raw = []
    for x in range(num_samples):
        data_raw.append(generate_average_data_sample(length))
    data = np.array(data_raw)

    norm_data = normalize_dataset(data)
        
    # 1) An input layer that takes input data as a matrix receives and passes it on
    X = norm_data[:, :-1]

    y = norm_data[:, -1].reshape(-1, 1)
    return X, y

def feedforward(X, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output):
    """
    feedforward returns the otputs of the activation function applied on the weight X feature + the bias
    a = f(wp + b)

    :X:                 input training data
    :w_input_to_hidden: weights used between the input and hidden layer
    :b_input_to_hidden: bias used between the input and hidden layer
    :w_hidden_to_output: weights used between the hidden and output layer
    :b_hidden_to_output: bias used between the hidden and output layer
    """
    # 5) Multiply the input by a set of weights (via matrix multiplication)
    # 2) A hidden layer 
    # 4) Weights between the layers
    z_input = np.dot(X, w_input_to_hidden) + b_input_to_hidden

    # 6) Apply deliberate activation function for every hidden layer
    a_input = activation_function(z_input)

    # 3) An output layer
    z_hidden = np.dot(a_input, w_hidden_to_output) + b_hidden_to_output
    a_hidden = activation_function(z_hidden)
    return a_input, a_hidden

def train(input_size):
    """
    train trains the neural network and returns the weights and biases of the model for prediciton
    
    :input_size: input_size determines how many features are in the input data
    """

    X, y = generate_average_data(50, input_size)

    # Recommended to have an amount of hidden layer neurons between the number of input features and output features
    hidden_Layer_neurons = 5
    output_neruons = 1

    # Initialize weights
    w_input_to_hidden = np.random.uniform(size=(input_size, hidden_Layer_neurons))
    w_hidden_to_output = np.random.uniform(size=(hidden_Layer_neurons, output_neruons))

    b_input_to_hidden = np.zeros((1, hidden_Layer_neurons))
    b_hidden_to_output = np.zeros((1, output_neruons))

    learning_rate = 0.001
    # 10) Repeat this process no less than 1,000 times to train the ANN
    epochs = 10000
    for x in range(epochs):
        a_input, a_hidden = feedforward(X, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output)

        #=== Back Propagation ===#
        # 8) Calculate error by taking the difference from the desired output and the predicted output, giving us the gradient descent to provide our loss function
        error_output = y - a_hidden
        delta_output = error_output * activation_derivative(a_hidden)

        # delta weight = eta X 
        hidden_layer_delta = np.dot(delta_output, w_hidden_to_output.T) * activation_derivative(a_input)

        # 9) Apply loss function to weights  
        w_hidden_to_output += np.dot(a_input.T, delta_output) * learning_rate
        b_input_to_hidden += np.sum(delta_output) * learning_rate

        w_input_to_hidden += np.dot(X.T, hidden_layer_delta) * learning_rate
        b_hidden_to_output += np.sum(delta_output) * learning_rate 

    return w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output

print("This program uses a neural network to predict the average of an input series of numbers")
print('Enter a series of numbers separated by commas (e.g. 1,2,3,4,5,6,7)')
user_input = input()
test_data = [int(e) for e in user_input.split(",")]
input_size = len(test_data)

# 7) Return an output
w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output = train(input_size)
a_input, a_hidden = feedforward(test_data, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output)

print(test_data)
test_input = np.array([test_data])
print("The average of the input numbers is: " + str(sum(test_data)/len(test_data)))
print("The neural network predicted the average to be: " + str(a_hidden[0][0]))
