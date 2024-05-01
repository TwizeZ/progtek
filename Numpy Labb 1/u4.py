import numpy as np
import matplotlib.pyplot as plt


def f4(x):
    return 1 + np.sin(x) + 0.5*np.cos(4*x)

def df4(x):
    return np.cos(x) - 2*np.sin(4*x)

def derivative(x, h):
    return (f4(x+h)-f4(x))/h

h = 0.01
x = np.arange(0, 10, 0.1)

plt.plot(x, f4(x))
plt.plot(x, df4(x))
plt.plot(x, derivative(x, h))

plt.grid(True)
plt.show()