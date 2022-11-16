from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y_train = np.array([58, 60, 80, 82, 82, 85, 88, 87, 85, 88, 70, 50])

m = len(x_train)
print(f"Number of training examples {m}")

i = 0

x_i = x_train[i]
y_i = y_train[i]

plt.scatter(x_train, y_train, marker='x', c='r')
plt.title('rice prices')
plt.ylabel('Price/kg')
plt.xlabel('months')
plt.show()

# initial values
w = 100
b = 100

def calculate_model_output(w, b, x):
    m = x.shape
    f_wb = np.zeros(m)
    for i in range(len(x)):
        f_wb[i] = w * x[i] + b

    return f_wb

temp_f_wb = calculate_model_output(w,b,x_train)
plt.plot(x_train, temp_f_wb, c='b', label = 'Our Prediction')
plt.scatter(x_train, y_train, marker='x', c='r', label = 'Actual Values')
plt.title('rice prices')
plt.ylabel('Price/kg')
plt.xlabel('months')
plt.legend()
plt.show()

# prediction
w = 100
b = 200
