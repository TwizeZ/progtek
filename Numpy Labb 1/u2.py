import numpy as np


def function_a(x):
    return x**2


def function_b1(x):
    return x*x


def function_b2(x):
    return x@x


def function_c1(x):
    return x*x


def function_c2(x):
    return x@x

x = 2
y = np.array([1, 2, 3])
z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(function_a(x))
print(function_b1(y))
print(function_b2(z[0]))
print(function_c1(z))
print(function_c2(z))