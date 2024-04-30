import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

# Uppgift 1

a = np.arange(1,6)

b = np.arange(0.0, 2*np.pi, 0.1)

c = np.array([[1,2],[3,4],[5,6]])

d = np.append(a, [6,7])

e_shape = np.array(a.tolist() + np.arange(-5, 0, 1).tolist())
e = e_shape.reshape(2, 5)

f = np.sin(b)





# Uppgift 2

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





# Uppgift 3

def f3(x):
    return 1 + x + 4/((x-2)*(x-2))


def asymptote(x):
    return 1 + x


x = np.arange(-10, 10, 0.1)
y = f3(x)
y_asym1 = asymptote(x)
y_asym2 = 2

# plt.plot(x, y)
# plt.plot(x, y_asym1)
# plt.vlines(y_asym2, -10, 10, colors="green")

# plt.axis([-10, 10, -10, 10])
# plt.grid(True)
# plt.show()





# Uppgift 4

def f4(x):
    return 1 + np.sin(x) + 0.5*np.cos(4*x)

def df4(x):
    return np.cos(x) - 2*np.sin(4*x)

def derivative(x, h):
    return (f4(x+h)-f4(x))/h

h = 0.01
x = np.arange(0, 10, 0.1)

# plt.plot(x, f4(x))
# plt.plot(x, df4(x))
# plt.plot(x, derivative(x, h))

# plt.grid(True)
# plt.show()





# Uppgift 5

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





# Uppgift 6

def f6(t, A, B):
    return np.e**(-t) * (A*np.cos(t) + B*np.sin(t)) + np.cos(t) + 2*np.sin(t)

x = np.arange(0, 10, 1/81)

for A in range(-4, 5):
    for B in range(-4, 5):
        # plt.plot(x, f6(x, A, B))
        pass

# plt.grid(True)
# plt.show()





# Uppgift 7

def sine(x):
    return np.sin(x)


def taylor(x, k):
    sumval = 0
    for i in range(0, k+1):
        sumval = sumval + (((-1)**i * x**(1 + 2*i)) / (math.factorial(1 + 2*i)))
    return sumval

k = 13
x = np.arange(-15, 15, 0.01)

# plt.plot(x, sine(x))
# plt.plot(x, taylor(x, k), color="purple")

# plt.axis([-15, 15, -2, 2])
# plt.grid(True)
# plt.show()





# Uppgift 8

# a

def f8a(x):
    return x - np.cos(x)

x = np.arange(-10, 10, 0.1)
y1 = x
y2 = np.cos(x)

# plt.plot(x, f8a(x), color='purple')
# plt.plot(x, y1, color='green')
# plt.plot(x, y2, color='blue')

# plt.grid(True)
# plt.show()

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
# print("Felet: " + str(f8a(bisection)))

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
print()

# d

print("Counter Bisection: " + str(b_counter))
print("Counter Newton: " + str(n_counter))

# e

print("Scipy: " + str(sp.optimize.fsolve(f8a, a)))





# Uppgift 9

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)



# a - sfär

def plot_sphere():
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z



# b - kon

def plot_cone():
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), -np.sin(v))
    return x, y, z



# c - pyramid

def plot_pyramid(base_center, base_side_length, height):
    # Define the vertices of the base
    base_vertices = np.array([
        [base_center[0] - base_side_length / 2, base_center[1] - base_side_length / 2, base_center[2]],
        [base_center[0] + base_side_length / 2, base_center[1] - base_side_length / 2, base_center[2]],
        [base_center[0] + base_side_length / 2, base_center[1] + base_side_length / 2, base_center[2]],
        [base_center[0] - base_side_length / 2, base_center[1] + base_side_length / 2, base_center[2]]
    ])

    # Define the apex of the pyramid
    apex = np.array([base_center[0], base_center[1], base_center[2] + height])

    # Vertices of each triangular face
    vertices = [
        [base_vertices[0], base_vertices[1], apex],
        [base_vertices[1], base_vertices[2], apex],
        [base_vertices[2], base_vertices[3], apex],
        [base_vertices[3], base_vertices[0], apex],
        [base_vertices[0], base_vertices[1], base_vertices[2]],
        [base_vertices[0], base_vertices[2], base_vertices[3]]
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vertex_set in vertices:
        xs = [vertex[0] for vertex in vertex_set]
        ys = [vertex[1] for vertex in vertex_set]
        zs = [vertex[2] for vertex in vertex_set]
        ax.plot(xs, ys, zs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


# Plots the functinons
# x, y, z = plot_sphere()
# x, y, z = plot_cone()
# plot_pyramid(np.array([0, 0, 0]), 4, 5)



# Plot the surface
# ax.plot_surface(x, y, z)

# Set an equal aspect ratio
# ax.set_aspect('equal')

# plt.show()



# d - halvsfär

def plot_half_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi/2, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Plot the surface
    ax.plot_surface(x, y, z)

    # Set an equal aspect ratio
    ax.set_aspect('equal')

    plt.show()

    # Två spiraler som snurrar runt varandra

    ax = plt.figure().add_subplot(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='parametric curve')
    ax.plot(y, x, z, label='parametric curve')
    ax.legend()

    plt.show()

# plot_half_sphere()



# Uppgift 10

# a

a = np.array([[4, -1, -9, -4, -6], [1, 1, -1, 4, -5], [0, -3, 4, 7, 0], [3, -5, -5, -3, 7], [9, -1, 4, -8, -9]])
b = np.array([-59, -21, 20, 16, -11])
x = np.linalg.solve(a, b)

print("x1:", x.item(0), "x2:", x.item(1), "x3:", x.item(2),"x4: ", x.item(3), "x5:", x.item(4))

# b

def price(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        price_list = []
        for i, line in enumerate(file):
            if i < 2:
                continue
            elements = line.split()
            price_list.append(float(elements[1]))
        return price_list


def kilometres(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        kilometres_list = []
        for i, line in enumerate(file):
            if i < 2:
                continue
            elements = line.split()
            kilometres_list.append(float(elements[2]))
        return kilometres_list


file = "/Users/felix/Documents/University/Prog/progtek/Numpy Labb 1/Shinkansen.text"
x = np.array(kilometres(file))
y = np.array(price(file))

print()
print(x)
print(y)

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()

def price_2(x):
    return m*x + c

print(f"\nSendai - Tokyta: {price_2(325.4)} JPY")
print(f"Stockholm - Göteborg: {price_2(455)*0.07} SEK\n")

# c

nutrients_dict = {}
behov_list = []

def read_nutrients(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        for i, line in enumerate(file):
            if line == "\n" or line == "":
                break

            if i < 2:
                continue

            elements = line.split()
            for item in elements:
                item.replace(" ", "")
            
            nutrients_dict[elements[0]] = {"protein":float(elements[1]),
                                      "carbonhydrates":float(elements[2]),
                                      "fat":float(elements[3]),
                                      "A":float(elements[4]),
                                      "B1":float(elements[5]),
                                      "B2":float(elements[6]),
                                      "B3":float(elements[7]),
                                      "B12":float(elements[8]),
                                      "C":float(elements[9]),
                                      "D":float(elements[10]),
                                      "K":float(elements[11]),
                                      "energy":float(elements[12]),
                                      "price":float(elements[13])}
        return nutrients_dict


def read_behov(file_name):
    with open(file_name, "r", encoding="utf8") as file:
        line = file.readlines()[-1]
        elements = line.split()
        for item in elements:
            behov_list.append(float(item[:-1]))
        
        return behov_list


behov = read_behov("Naringsbehov.text")
nutrients = read_nutrients("nutrients.text")

for _, value in nutrients.items():
    for prop in value:
        print(prop[-1])

# c = array
read_nutrients("nutrients.text")
