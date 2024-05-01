import numpy as np
import matplotlib.pyplot as plt


def f6(t, A, B):
    return np.e**(-t) * (A*np.cos(t) + B*np.sin(t)) + np.cos(t) + 2*np.sin(t)

x = np.arange(0, 10, 1/81)

for A in range(-4, 5):
    for B in range(-4, 5):
        plt.plot(x, f6(x, A, B))

plt.grid(True)
plt.show()