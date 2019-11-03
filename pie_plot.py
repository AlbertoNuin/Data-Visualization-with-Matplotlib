#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:28:04 2019

Pie chart

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.025, 0.025, 0.95, 0.95])

# The explode parameter for all makes it look like white lines
# List comprehension in colors to change the shade of gray
plt.pie(Z, explode=Z*0.05, colors=['%f' % (i/float(n)) for i in range(n)])

# This ensures a perfect circle 
plt.axis('equal')

# Save figure using 72 dots per inch
plt.savefig('pie_plot.png', dpi=72)

plt.show()
