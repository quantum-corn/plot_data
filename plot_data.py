# %% md
# # Plot Data
# A simple matplotlib and numpy based python code to quickly plot 2D data
# ### v1.0

# %% imports
import matplotlib.pyplot as plt
import numpy as np

# %% function creation
x=(1, 2, 3, 4, 7, 9)
y=(0.9, 7.8, 5.6, 6.7, 8.7, 4.9)

# %% plot
fig, ax=plt.subplots()
ax.plot(x, y)

# %% grid setup
ax.set(xlim=(0,10), xticks=np.arange(1,10), ylim=(0,10), yticks=np.arange(1,10))

# %% display the plot
plt.show()
