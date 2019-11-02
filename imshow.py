#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 07:22:51 2019

Imshow

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 15
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)

# Control the size of the axes
plt.axes([0.025, 0.025, 0.95, 0.95])

# Change the default origin ('upper': matrix convention) to 'lower'
plt.imshow(f(X, Y), interpolation='nearest', cmap='bone', origin='lower')

# Add a colorbar
plt.colorbar()

# Remove xticks and yticks for a clean chart
plt.xticks(())
plt.yticks(())

# Save figure using 72 dots per inch
plt.savefig('imshow.png', dpi=72)

plt.show()
