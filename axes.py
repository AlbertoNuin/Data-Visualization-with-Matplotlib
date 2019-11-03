#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:49:54 2019

Axes: plots within plots

@author: alberto
"""

import matplotlib.pyplot as plt

# Draws a default (1 x 1) chart in data units
# List shows first the xy coordinates of the bottom left hand corner,
# and then the xy coordinates of the top right hand corner
plt.axes([.1, .1, .8, .8])
# Removes the default ticks in the x and y axis
plt.xticks(()), plt.yticks(())
# Annotation: position in axes, label, horizontal and vertical alignment
# Font size and transparency
plt.text(.6, .6, 'axes([.1, .1, .8, .8])', ha='center', va='center',
         size=20, alpha=.5)

# Draws a second axes inside the area of the previous axes
# Fine tune its coordinates to align it to corners, make it overlap, etc.
plt.axes([.2, .2, .3, .3])
plt.xticks(()), plt.yticks(())
plt.text(.5, .5, 'axes([.2, .2, .3, .3])', ha='center', va='center',
         size=16, alpha=.5)

# Save figure using 72 dots per inch
plt.savefig('axes.png', dpi=72)


plt.show()