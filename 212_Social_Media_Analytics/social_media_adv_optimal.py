# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:56:04 2025

@author: Tanyamol
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for YT and FB
YT = np.arange(30, 351, 1)
FB = np.arange(5, 20, 1)

# Create a meshgrid for YT and FB
YT, FB = np.meshgrid(YT, FB)

# Calculate Sales Revenue

# Calculate Sales Revenue
Sales_Q = (3.50 + YT * 0.045 + FB * 0.187)
Sales_Revenue = Sales_Q*(30-Sales_Q)/0.5


# Calculate Cost
Cost = 200 + 0.001 * YT ** 1.5 + 0.02 * FB ** 1.5

# Calculate the difference
Difference = Sales_Revenue - Cost

# Find the maximum point
max_diff = np.max(Difference)
max_index = np.unravel_index(np.argmax(Difference), Difference.shape)
max_YT = YT[max_index]
max_FB = FB[max_index]

# Print the coordinates of the maximum point
print(f"Maximum Difference: {max_diff}")
print(f"Coordinates of Maximum Point: YT = {max_YT}, FB = {max_FB}")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Sales Revenue
ax.plot_surface(YT, FB, Sales_Revenue, cmap='Blues', alpha=0.7, label='Sales Revenue')

# Plot Cost
ax.plot_surface(YT, FB, Cost, cmap='gray', alpha=0.7, label='Cost')

# Plot the difference
surface = ax.plot_surface(YT, FB, Difference, cmap='coolwarm', alpha=0.7)

# Plot the maximum point
ax.scatter(max_YT, max_FB, max_diff, color='red', s=100, label='Max Point')

# Labels
ax.set_xlabel('YT')
ax.set_ylabel('FB')
ax.set_zlabel('Difference')

# Title
ax.set_title('Difference Between Sales Revenue and Cost')

# Rotate the plot by 45 degrees
ax.view_init(elev=5, azim=60)

# Add color bar for surface plot
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

# Legend
ax.legend()

plt.show()



