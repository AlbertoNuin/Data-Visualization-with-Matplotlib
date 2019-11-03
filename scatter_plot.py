#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:34:35 2019

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

# Scatter plot parameters
# c: color determined by angle of (X,Y)
# s: marker size
# alpha: transparency

plt.scatter(X, Y, c=np.angle(X+Y*1j), s=75, alpha=0.6)

# Hide axis labels
plt.xticks(())
plt.yticks(())

# Zoom window
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Save figure using 72 dots per inch
plt.savefig('scatter_plot.png', dpi=72)

plt.show()
