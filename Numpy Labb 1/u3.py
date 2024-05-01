import numpy as np
import matplotlib.pyplot as plt


def f3(x):
    return 1 + x + 4/((x-2)*(x-2))


def asymptote(x):
    return 1 + x


x = np.arange(-10, 10, 0.1)
y = f3(x)
y_asym1 = asymptote(x)
y_asym2 = 2

plt.plot(x, y)
plt.plot(x, y_asym1)
plt.vlines(y_asym2, -10, 10, colors="green")

plt.axis([-10, 10, -10, 10])
plt.grid(True)
plt.show()