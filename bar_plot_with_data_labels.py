#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:05:33 2019

Bar plot with data labels

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# Label the blue bars with data
# Fine-tune manually position of test by trial and error
for x, y in zip(X, Y1):
    plt.text(x + 0.1, y + 0.05, '%.2f' % y,
             ha='center', va='bottom')

# Label the red bars with data
for x, y in zip(X, Y2):
    plt.text(x + 0.1, - y - 0.15, '%.2f' % y,
             ha='center', va='bottom')

# Set y limits
plt.ylim(-1.25, +1.25)

# Hide axis
plt.axis('off')

# Save figure using 72 dots per inch
plt.savefig('bar_plot_with_data_labels.png', dpi=72)

plt.show()
