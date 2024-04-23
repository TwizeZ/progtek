import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Uppgift 1

a = np.arange(1,6)

b = np.arange(0.0, 2*np.pi, 0.1)

c = np.array([[1,2],[3,4],[5,6]])

d = np.append(a, [6,7])

e = np.append(a, np.arange(-5, 0), 1)

f = np.sin(b)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)