import numpy as np


def integral_a(x):
    return x/((x**2+4)**(1/3))


def integral_b(x):
    return np.sqrt(x)*np.log(x)


def riemann_sum(f, a, b, n):
    sumval = 0
    h = (b-a)/n
    for i in range(0,n-1):
        current_x = a+(i*h)
        sumval = sumval + f(current_x) * h
    return sumval

n = 10
print(riemann_sum(integral_a, 0, 2, n))
print(riemann_sum(integral_b, 1, 4, n))