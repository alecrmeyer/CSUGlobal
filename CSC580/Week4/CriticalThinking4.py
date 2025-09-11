import numpy as np

#1) Generate the synthetic data
N = 100

# Zeros form a Gaussian centered at (-1, -1)
x_zeros = np.random.multivariate_normal(mean=np.array((-1, -1)), cov=.1*np.eye(2), size=(N//2,))
y_zeros = np.zeros((N//2,))

# Ones form a Gaussian centered at (1, 1)
x_ones = np.random.multivariate_normal(mean=np.array((1, 1)), cov=.1*np.eye(2), size=(N//2,))
y_ones = np.ones((N//2,))

x_np = np.vstack([x_zeros, x_ones])
y_np = np.concatenate([y_zeros, y_ones])
print(x_np.shape)

#2) Plot x_zeros and x_ones
import matplotlib.pyplot as plt
plt.scatter(x_zeros[:, 0], x_zeros[:, 1], color='blue', label='Class 0')
plt.scatter(x_ones[:, 0], x_ones[:, 1], color='red', label='Class 1')
plt.title("Training Data")  
#plt.show()

#3) Generate TensorFlow Model
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

with tf.name_scope("placeholders"):
  x = tf.compat.v1.placeholder(tf.float32, (N, 2))
  y = tf.compat.v1.placeholder(tf.float32, (N,))

with tf.name_scope("weights"):
  W = tf.Variable(tf.random.normal((2, 1)))
  b = tf.Variable(tf.random.normal((1,)))

with tf.name_scope("prediction"):
  y_logit = tf.squeeze(tf.matmul(x, W) + b)
  # the sigmoid gives the class probability of 1
  y_one_prob = tf.sigmoid(y_logit)
  # Rounding P(y=1) will give the correct prediction.
  y_pred = tf.round(y_one_prob)

 
with tf.name_scope("loss"):
  # Compute the cross-entropy term for each datapoint
  entropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=y_logit, labels=y)
  # Sum all contributions
  l = tf.reduce_sum(entropy)

with tf.name_scope("optim"):
  train_op = tf.compat.v1.train.AdamOptimizer(.01).minimize(l)

with tf.name_scope("summaries"):
  tf.summary.scalar("loss", l)
  merged = tf.summary.merge_all()

train_writer = tf.summary.FileWriter('logistic-train', tf.get_default_graph())

training_epochs = 1000

with tf.Session() as sess:
    # Initializing the variables
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_epochs):
        sess.run(train_op, feed_dict = {x: x_np, y: y_np})
        sess_cost = sess.run(l, feed_dict = {x: x_np, y: y_np})


    #8) Plotting the regression line
    plt.scatter(x_zeros[:, 0], x_zeros[:, 1], color='blue', label='Class 0')
    plt.scatter(x_ones[:, 0], x_ones[:, 1], color='red', label='Class 1')
    weight_final = sess.run(W)
    bias_final = sess.run(b)

    decision_boundary_x = np.array([np.min(x_np[:, 0]), np.max(x_np[:, 0])])
    decision_boundary_y = (- 1.0 / weight_final[0]) * (decision_boundary_x * weight_final + bias_final)
    decision_boundary_y = [sum(decision_boundary_y[:, 0]), sum(decision_boundary_y[:, 1])]
    plt.plot(decision_boundary_x, decision_boundary_y, color='green')
    plt.title("Training Data")
    plt.xlabel("x") 
    plt.ylabel("y")
    plt.show()

