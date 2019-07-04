import helpers
import SSAAE as SSAAE
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt


# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
idx_unlabel = np.random.randint(0, x_train.shape[0], 20000)
y_train[idx_unlabel] = 10
x_train = x_train.astype(np.float32) / 255.
x_test = x_test.astype(np.float32) / 255.
ann = SSAAE.SSAAE()
vecs, b = ann.generateRandomVectors(1000 * list(range(10)))
plt.scatter(vecs[:, 0], vecs[:, 1])
ann.train(x_train, y_train, x_test, y_test, epochs=10000)
vecs, b = ann.generateRandomVectors(1000 * list(range(10)))
generated = ann.decoder.predict(vecs)
print(generated.shape)
L = helpers.approximateLogLiklihood(generated, x_test)
print("Log Likelihood")
print(L)