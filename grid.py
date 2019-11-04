#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:35:03 2019

Grid

@author: alberto
"""

import matplotlib.pyplot as plt

ax = plt.axes([0.025, 0.025, 0.95, 0.95])
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)

ax.xaxis.set_major_locator(plt.MultipleLocator(1.))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))

ax.yaxis.set_major_locator(plt.MultipleLocator(1.))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')

ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

# Save figure using 72 dots per inch
plt.savefig('grid.png', dpi=72)


plt.show()
