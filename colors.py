#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:56:55 2019

Colors

@author: alberto
"""

import matplotlib.pyplot as plt

size = 10, 5
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=size, dpi=dpi)
fig.patch.set_alpha(0)
plt.axes([0, 0.1, 1, .8], frameon=False)

# This shows sequence of 11 colors - then they're cyclic
for i in range(1, 11):
    plt.plot([i, i], [0, 1], lw=30)
    
# plt.xlim(0, 11)
plt.xticks(()), plt.yticks(())

# Save figure using 72 dots per inch
plt.savefig('colors.png', dpi=72)


plt.show()