import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


# a

def A():
    img = plt.imread('maxresdefault.jpg')
    img_bw = np.zeros_like(img)

    for i in range(len(img)):
        for k in range(len(img[i])):
            img_bw_pixel_value = np.sum(img[i][k]) / 3
            img_bw[i][k] = [img_bw_pixel_value, img_bw_pixel_value, img_bw_pixel_value]


    plt.imshow(img_bw)
    plt.show()


# b

def B():
    img = plt.imread('maxresdefault.jpg')
    img_bw = img[:, :, 0] / 3 + img[:, :, 2] / 3

    Gx = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))
    Gy = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]))

    xd = sp.ndimage.convolve(img_bw, Gx, mode='constant')
    yd = sp.ndimage.convolve(img_bw, Gy, mode='constant')

    s = np.sqrt(xd**2 + yd**2)
    plt.imshow(s, cmap='gray')
    plt.show()
    return s

# c

def C():
    threshold = 50          # standard: 100 (0-255)

    s = B()
    for i in range(len(s)):
        for k in range(len(s[i])):
            if s[i][k] >= threshold:
                s[i][k] = 0
            elif s[i][k] < threshold:
                s[i][k] = 255

    plt.imshow(s, cmap='gray')
    plt.show()

A()
C()