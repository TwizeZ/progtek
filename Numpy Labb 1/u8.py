import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# a

def f8a(x):
    return x - np.cos(x)

x = np.arange(-10, 10, 0.1)
y1 = x
y2 = np.cos(x)

plt.plot(x, f8a(x), color='purple')
plt.plot(x, y1, color='green')
plt.plot(x, y2, color='blue')

plt.grid(True)
plt.show()

# b

def bisect(a, b):
    c = (a-b)/2
    counter = 0
    while abs(a-b) >= 10**-12:
        if f8a(c) == 0:
            return c, counter
        elif f8a(c) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
        counter += 1
    return c, counter

a = 0.1
b = 1.

print()
bisection, b_counter = bisect(a, b)
print("Bisect: " + str(bisection))

#c

def derivative_f8(x):
    return 1 + np.sin(x)

def newton_raphson(a):
    x = a
    x_0 = 0
    counter = 0
    while abs(x-x_0) > 10**-12:
        x_0 = x
        x = x - f8a(x)/derivative_f8(x)
        counter += 1
    return x, counter

newton, n_counter = newton_raphson(a)
print("Newton-Raphson: " + str(newton))

# d

print()
print("Counter Bisection: " + str(b_counter))
print("Counter Newton: " + str(n_counter))

# e

print()
print("Scipy: " + str(sp.optimize.fsolve(f8a, a)))