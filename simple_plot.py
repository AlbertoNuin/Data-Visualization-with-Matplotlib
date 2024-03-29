#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:32:53 2019

simple_plot

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 4), dpi=72)
axes = fig.add_axes([0.01, 0.01, .98, .98])
x = np.linspace(0, 2, 200, endpoint=True)
y = np.sin(2 * np.pi * x)
plt.plot(x, y, lw=.25, c='k')
plt.xticks(np.arange(0.0, 2.0, 0.1))
plt.yticks(np.arange(-1.0, 1.0, 0.1))
plt.grid()

plt.show()