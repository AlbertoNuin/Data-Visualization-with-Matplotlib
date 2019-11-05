#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:08:14 2019

Quiver: vector field

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10
X, Y = np.mgrid[0:n, 0:n]
T = np.arctan2(Y - n / 2., X - n / 2.)
R = 10 + np.sqrt((Y - n / 2.) ** 2 + (X - n / 2.) ** 2)
U, V = R * np.cos(T), R * np.sin(T)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.quiver(X, Y, U, V, R, alpha=0.5)
plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=0.5)

plt.xlim(-1, n), plt.xticks(())
plt.ylim(-1, n), plt.yticks(())

# Save figure using 72 dots per inch
plt.savefig('quiver.png', dpi=72)

plt.show()
