import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# a


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 100:
        z = z*z + c
        n += 1
    return True if n == 100 else False


# b


M = np.zeros((401, 401))

for i, a in enumerate(np.arange(-2, 2, 0.01)):
    for k, b in enumerate(np.arange(-2, 2, 0.01)):
        result = mandelbrot(a+b*1j)
        if result:
            M[i, k] = 1

plt.imshow(M, cmap='gray', extent=(-2, 2, -2, 2))
plt.show()


# c


N = np.zeros((401, 401))

for i, a in enumerate(np.arange(-1, -0.6, 0.001)):
    for k, b in enumerate(np.arange(0, 0.4, 0.001)):
        result = mandelbrot(a+b*1j)
        if result:
            N[i, k] = 1
        else:
            N[i, k] = 0

plt.imshow(N, cmap='gray', extent=(-2, 2, -2, 2))
plt.show()