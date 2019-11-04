#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:48:00 2019

Subplots using the stateful approach

@author: alberto
"""

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)

# Top landscape sized sub-plot
plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())
# Coordinates in plt.text are relative to plot assumed as 1x1
plt.text(0.5, 0.5, 'subplot(2, 1, 1)', ha='center', va='center',
         size=24, alpha=0.5)

# Square-sized plot in bottom, left-hand corner
plt.subplot(2, 3, 4)
plt.xticks(()), plt.yticks(())

# Square-sized plot in bottom, middle
plt.subplot(2, 3, 5)
plt.xticks(()), plt.yticks(())

# Square-sized plot in bottom, right-hand corner
plt.subplot(2, 3, 6)
plt.xticks(()), plt.yticks(())

# Clean residual white spaces for a cleaner, tighter look
plt.tight_layout()
plt.show()

# Save figure using 72 dots per inch
plt.savefig('subplots.png', dpi=72)

