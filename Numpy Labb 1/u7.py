import numpy as np
import matplotlib.pyplot as plt
import math


def sine(x):
    return np.sin(x)


def taylor(x, k):
    sumval = 0
    for i in range(0, k+1):
        sumval = sumval + (((-1)**i * x**(1 + 2*i)) / (math.factorial(1 + 2*i)))
    return sumval

k = 13
x = np.arange(-10, 10, 0.01)

plt.plot(x, sine(x))
plt.plot(x, taylor(x, k), color="purple")

plt.axis([-10, 10, -2, 2])
plt.grid(True)
plt.show()