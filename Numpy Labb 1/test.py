import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x2 = x[:2, 1:3]
print(x2)
print(x2.shape)

a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)

A = np.array([[1, 2], [3, 4]])
c = np.array([5, 6])
print(A@c)
print(A*c)

#-------------------------

arrayer = np.zeros((100,100,3))
arrayer[80,20] = [100, 100, 100]
plt.imshow(arrayer)
plt.show()