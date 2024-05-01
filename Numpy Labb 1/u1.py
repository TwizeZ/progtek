import numpy as np

a = np.arange(1,6)

b = np.arange(0.0, 2*np.pi, 0.1)

c = np.array([[1,2],[3,4],[5,6]])

d = np.append(a, [6,7])

e_shape = np.array(a.tolist() + np.arange(-5, 0, 1).tolist())
e = e_shape.reshape(2, 5)

f = np.sin(b)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)