#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:28:22 2019

@author: alberto
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a figure of sixe 8x6 inches, 80 dots per inch
plt.figure(figsize=(10, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue continuous line of width 1(pixels)
plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-', label='cosine')

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color='red', linewidth=2.5, linestyle='-', label='sine')

# Set x limits
plt.xlim(X.min()*1.1, X.max()*1.1)

# Set x ticks
x_sym = [r'$-\pi$', r'$-\pi/2$', '', r'$+\pi/2$', r'$+\pi$']
plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True), x_sym)

# Set y limits
plt.ylim(C.min()*1.1, C.max()*1.1)

# Set y ticks
y_sym = [r'$-1$', r'0', r'$+1$']
plt.yticks(np.linspace(-1, 1, 3, endpoint=True), y_sym)

# Moving spines
ax = plt.gca()   # get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# Add legend (requires adding kwarg label in plot)
plt.legend(loc='upper left')

# Annotate points
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
C_note = r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$'
plt.annotate(C_note,
             xy=(t, np.cos(t)),
             xycoords='data',
             xytext=(-90, -50),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(
                     arrowstyle='->',
                     connectionstyle='arc3,rad=.2'))
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle='--')
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
S_note = r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$'
plt.annotate(S_note,
             xy=(t, np.sin(t)),
             xycoords='data',
             xytext=(10, 30),
             textcoords='offset points',
             fontsize=16,
             arrowprops=dict(
                     arrowstyle='->',
                     connectionstyle='arc3,rad=.2'))

# Make the tick labels more visible
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(
            facecolor='white',
            edgecolor='None',
            alpha=0.65))

# Save figure using 72 dots per inch
plt.savefig('exercise2.png', dpi=72)

plt.show()
