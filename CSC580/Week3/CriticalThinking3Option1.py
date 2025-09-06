import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt

np.random.seed(101)

tf.random.set_seed(101)

#Now, let’s generate some random data for training the Linear Regression Model.

# Generating random linear data

# There will be 50 data points ranging from 0 to 50

x = np.linspace(0, 50, 50)

y = np.linspace(0, 50, 50)

# Adding noise to the random linear data

x += np.random.uniform(-4, 4, 50)

y += np.random.uniform(-4, 4, 50)

n = len(x) # Number of data points

plt.scatter(x, y)
plt.show()

X = tf.placeholder("float")
Y = tf.placeholder("float")

weight = tf.Variable(np.random.randn(), name = "weight")
bias = tf.Variable(np.random.randn(), name = "bias")

learning_rate = 0.01
training_epochs = 1000

# Hypothesis
y_hat = tf.add(tf.multiply(X, weight), bias)

# Cost Function - MSE
cost_function = tf.reduce_sum(tf.pow(y_hat - Y, 2)) 

# Optimizer Function - Gradient Descent
optimizer_function = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)


