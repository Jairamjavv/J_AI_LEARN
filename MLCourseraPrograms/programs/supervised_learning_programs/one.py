import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1, 2])
y_train = np.array([200, 350])

m = len(x_train)
print(f"Number of training examples {m}")

i = 0

x_i = x_train[i]
y_i = y_train[i]

plt.scatter(x_train, y_train, marker='x', c='r')
plt.title('rice prices')
plt.ylabel('Price in 1000s')
plt.xlabel('Kgs')
plt.show()

# initial values
w = 100
b = 100

def calculate_model_output(w, b, x):
    m = x.shape
    f_wb = np.zeroes(m)
    for i in range(len(x)):
        f_wb[i] = w * x[i] + b

    return f_wb