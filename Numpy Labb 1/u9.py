import numpy as np
import matplotlib.pyplot as plt


# sfär

def plot_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    
    ax.plot_surface(x, y, z)
    ax.set_aspect('equal')
    plt.show()



# a - kon

def plot_cone():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), -np.sin(v))
    
    ax.plot_surface(x, y, z)
    ax.set_aspect('equal')
    plt.show()



# b - pyramid

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



# c - halvsfär

def plot_half_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi/2, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z)
    ax.set_aspect('equal')
    plt.show()



# d - spir

def spiral():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Prepare arrays x, y, z
    theta1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    theta2 = np.linspace(-4 * np.pi + np.pi, 4 * np.pi + np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = 1
    x1 = r * np.sin(theta1)
    y1 = r * np.cos(theta1)
    x2 = r * np.sin(theta2)
    y2 = r * np.cos(theta2)

    ax.plot(x1, y1, z, label='parametric curve')
    ax.plot(x2, y2, z, label='parametric curve')
    ax.legend()

    plt.show()



# Plots the functinons
plot_sphere()
plot_cone() # a
plot_pyramid(np.array([0, 0, 0]), 4, 5) # b
plot_half_sphere() # c
spiral() # d