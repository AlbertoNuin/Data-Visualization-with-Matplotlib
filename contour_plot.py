#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:23:06 2019

Contour plot

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# Create coordinate matrices from coordinate vectors
X, Y = np.meshgrid(x, y)

# contourf fills between contour lines using cmap
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap='hot')

# contour draws contour lines and saves as CoutourSet object
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)

# pass ContourSeet object to command clabel to label the contour lines
plt.clabel(C)

# Hide axis
plt.axis('off')

# Save figure using 72 dots per inch
plt.savefig('contour_plot.png', dpi=72)

plt.show()