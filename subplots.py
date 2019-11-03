#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:48:00 2019

Subplots

@author: alberto
"""

import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)

# Top landscape sized sub-plot
plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

# Square-sized plot in bottom, left-hand corner
plt.subplot(2, 3, 4)
plt.xticks(()), plt.yticks(())

# Square-sized plot in bottom, middle
plt.subplot(2, 3, 5)
plt.xticks(()), plt.yticks(())

# Square-sized plot in bottom, right-hand corner
plt.subplot(2, 3, 6)
plt.xticks(()), plt.yticks(())

# Save figure using 72 dots per inch
plt.savefig('subplots.png', dpi=72)

plt.show()