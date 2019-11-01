#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:28:22 2019

Line plots using the fill_between command

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X, Y + 1, color='blue', alpha=1)
# Fill between sine curve and 'zero' (y = 1) - hatch
plt.fill_between(X, Y+1, 1, color='blue', alpha=0.4, hatch='...')

plt.plot(X, Y - 1, color='blue', alpha=1)

# Fill between 'negative' sine curve and 'zero' (y = -1)
# Use linewidth = 0 to keep y = -1 clean 
# Hatch
plt.fill_between(X, np.minimum(Y - 1, -1), -1, 
                 color='red', alpha=0.4, hatch='|||', linewidth=0)

# Fill between 'positive' sine curve and 'zero' (y = -1)
plt.fill_between(X, np.maximum(Y - 1, -1), -1, 
                 color='blue', alpha=0.4, linewidth=0)

# Hide axis
plt.axis('off')

# Save figure using 72 dots per inch
plt.savefig('lineplot_fill_between.png', dpi=72)

plt.show()
