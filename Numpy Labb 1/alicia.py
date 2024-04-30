# Alicia Nordström, Vanessa Tang
# Numpy lab1 3/5-23
# DD1318

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import approximate_taylor_polynomial
from scipy.optimize import fsolve
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

# Uppgift 1

a = np.array([1, 2, 3, 4, 5])
b = np.arange(0, 2*np.pi, 0.1)
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array(a.tolist() + [6, 7])
e = np.array(a.tolist() + [-1, -2, -3, -4, -5]).reshape(2, 5)
f = np.sin(b)

# Uppgift 2


def function_a(x):
    return x*x


def function_b1(x):
    return x*x


def funtion_b2(x):
    return x@x


def function_c1(x):
    return x*x


def function_c2(x):
    return x@x


# Uppgift 3

def my_f1(x):
    return 1 + x + 4/((x-2)**2)


def my_s_asymptote(x):
    return x + 1


x = np.arange(-10, 10, 0.1)
y = my_f1(x)
y_asym = my_s_asymptote(x)

plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.plot(x,y)
plt.plot(x,y_asym)
plt.vlines(2, -10, 10, colors="orange")
plt.show()

# Uppgift 4

"""def my_f2(x):
    return 1 + np.sin(x) + 0.5*np.cos(4*x)

def my_f2_analytical_derivative(x):
    return np.cos(x)-2*np.sin(4*x)

def my_f2_numerical_derivative(x):
    h = 2
    return (my_f2(x+h) - my_f2(x-h)) / 2*h

h = 0.1
ddx_kernal = np.array([1/(2*h), 0, -1/(2*h)])

y2 = my_f2(x)
num_derivative = np.convolve(y2, ddx_kernal, mode='same')

y2_a = my_f2_analytical_derivative(x)
#y2_num = my_f2_numerical_derivative(x)"""

"""plt.ylim(-5,5)
plt.xlim(-3*np.pi, 3*np.pi)
#plt.plot(x, y2)
plt.plot(x,y2_a, color="blue")
plt.plot(x,num_derivative, color="red")
plt.show()"""

# Uppgift 5

"""def integrand1(x):
    return x/((x**2 + 4)**(1/3))

def integrand2(x):
    return np.sqrt(x)*np.log(x)

I1a = quad(integrand1, 0, 2)
I2a = quad(integrand2, 1, 4)

h5 = 0.0001
x5a = np.arange(0, 2, h5)
x5b = np.arange(1, 4, h5)
f_x = integrand1(x5a)
g_x = integrand2(x5b)

I1b = np.trapz(f_x, x5a)
I2b = np.trapz(g_x, x5b)

print("Scipy's calculation for f(x):", I1a)
print("Scipy's calculation for g(x):", I2a)
print("With Numpy .trapz for f(x):", I1b)
print("With Numpy .trapz for g(x):", I2b)"""

# Uppgift 6
"""
https://www.geeksforgeeks.org/how-to-build-an-array-of-all-combinations-of-two-numpy-arrays/
"""
"""
A = np.arange(-4, 5, 1)
B = np.arange(-4, 5, 1)

comb_array = np.array(np.meshgrid(A, B)).T.reshape(-1, 2) # .meshgrid - grid of al combinations

def q_t(t, A, B):
    return (np.e**(-t))*(A*np.cos(t) + B*np.sin(t)) + np.cos(t) + 2*np.sin(t)

x6 = np.arange(0, 10.1, 0.1)

print(comb_array)

for item in comb_array:
    A = item[0]
    B = item[1]
    y6 = q_t(x6, A, B)
    plt.plot(x6, y6)
    
plt.show()
"""
# Uppgift 7
"""
I denna uppgift skall ni beräkna och plotta Taylorpolynomet av grad 13 kring punkten t=0 till funktionen Sin(x). 
(minsta termen skall alltså vara x och största vara x^13). 
Har ni glömt bort hur formeln för Taylorutvecklingen av sin(x) ser ut kan ni titta här http://www.wolframalpha.com/input/?i=taylor+series+sin+x

Plotta sin(x) för x från -10 till 10
Plotta ert taylorpolynom
För vilka x är approximationen bra respektive dålig? Plotta differensen mellan polynomet och sinusfunktionen!
"""

x_7 = np.arange(-10, 10.1, 0.1)
f_7 = np.sin(x_7)
tp_13 = approximate_taylor_polynomial(np.sin, 0, 13, 1)

def difference(f1, f2):
    return f1-f2

plt.plot(x_7,f_7)
plt.plot(x_7,tp_13(x_7))
plt.plot(x_7, difference(f_7, tp_13(x_7)))
plt.axis([-10, 10, -10, 10])
plt.show()

# Uppgift 8a
x8a = np.arange(-10, 10, 0.1)


def y_8a(x):
    return x - np.cos(x)


"""plt.plot(x8a, x8a, color='green')
plt.plot(x8a, np.cos(x8a),color='green')
plt.plot(x8a, y8a(x8a), color='purple')
plt.show()"""

# Uppgift 8b
a = 0.1
b = 1.


def x_8b(a, b):
    counter_a = 0
    while abs(a - b) >= (10**-12):
        c = (b - a)/2 + a
        counter_a += 1
        if y_8a(c) < 0:
            a = c
        else:
            b = c
    return c, counter_a


svar_a, counter_a = x_8b(a, b)

print("Svaret:", svar_a)
print("Felet:", y_8a(svar_a))

# Uppgift 8c


def derivative_f(x):
    return 1 + np.sin(x)


def next_x(x):
    return x - (y_8a(x)/derivative_f(x))


def x_8c(a):
    x = a
    counter_b = 0
    while abs(next_x(x) - x) > 10**-12:
        x = next_x(x)
        counter_b += 1
    return x, counter_b


svar_b, counter_b = x_8c(a)

print("Svaret:", svar_b)
print("Felet:", (y_8a(svar_b)))  # inga decimaler??? Använd inte svaret utan jämför metoderna med varandra

# Uppgift 8d

print(counter_a)  # 8a itererar mest
print(counter_b)

new_svar_a, new_counter_a = x_8b(0.000001-(np.pi/2), b)
new_svar_b, new_counter_b = x_8c(0.000001-(np.pi/2))

print("Svar:", new_svar_a, "Felet:", y_8a(new_svar_a),
      "Iterationer:", counter_a)  # 8a itererar fortfarande mest
print("Svar:", new_svar_b, "Felet:", y_8a(
    new_svar_b), "Iterationer:", counter_b)


# Uppgift 8e
print("Fsolve:", fsolve(y_8a, [a]))

# Uppgift 9a

"""fig = plt.figure()
ax = fig.add_subplot(projection='3d')
u = np.linspace(0, 2 * np.pi, 100)  # theta
r = np.meshgrid(x,y)
x = np.outer(r, np.cos(u))
y = np.outer(r, np.sin(u))
z = np.outer(r,2)
ax.plot_surface(x, y, z)
ax.set_aspect('equal')
plt.show()"""

# Uppgift 9b

"""fig = plt.figure()
ax = fig.add_subplot(projection='3d')
p = np.array([[2, 0, 0], [0, 2, 0], [2, 2, 0], [0, 0, 0], [1, 1, 2]])
ax.scatter3D(p[:, 0], p[:, 1], p[:, 2])
verts = [[p[0], p[3], p[4]], [p[0], p[2], p[4]],
         [p[1], p[2], p[4]], [p[1], p[3], p[4]], [p[0], p[3], p[1], p[2]]]
ax.add_collection3d(Poly3DCollection(verts, facecolors='purple', linewidths=1, edgecolors='r', alpha=.25))
plt.show()"""


# Uppgift 9c

"""fig = plt.figure()
ax = fig.add_subplot(projection='3d')
u = np.linspace(0, 2 * np.pi, 100) #theta
v = np.linspace(0, np.pi/2, 100) #phi
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z)
ax.set_aspect('equal')
plt.show()"""

# Uppgift 9d

"""ax = plt.figure().add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z
x = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.plot(y, x, z, label='parametric curve')
ax.legend()
plt.show()"""

# Uppgift 10a
"""a_10a = np.array([[4, -1, -9, -4, -6], [1, 1, -1, 4, -5],
                 [0, -2, 4, 7, 0], [3, -5, -5, -3, 7], [9, -1, 4, -8, -9]])
b_10a = np.array([-59, -21, 20, 16, -11])
x_10a = np.linalg.solve(a_10a, b_10a)

print(x_10a)
print(np.allclose(np.dot(a_10a, x_10a), b_10a))"""

# Uppgift 10b
