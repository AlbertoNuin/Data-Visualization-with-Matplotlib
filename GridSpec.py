#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:10:56 2019

GridSpec: tiling different axes in the same figure

@author: alberto
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure(figsize=(6, 4))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks(()), plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=0.5)

axes_2 = plt.subplot(G[1, :-1])
plt.xticks(()), plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=0.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks(()), plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=0.5)

axes_4 = plt.subplot(G[2, 0])
plt.xticks(()), plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=0.5)

axes_5 = plt.subplot(G[2, -2])
plt.xticks(()), plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=0.5)

plt.tight_layout()

# Save figure using 72 dots per inch
plt.savefig('GridSpec.png', dpi=72)