import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import sys

# %matplotlib inline

# generate some random data
npoints = 5
x = np.random.randn(npoints)
y = np.random.randn(npoints)

# make the size proportional to the distance from the origin
s = [0.1 * np.linalg.norm([a, b]) for a, b in zip(x, y)]
s = [a / max(s) for a in s]  # scale

# set color based on size
c = s
colors = [cm.jet(color) for color in c]  # gets the RGBA values from a float
labels=range(npoints)

# create a new figure
plt.figure()
ax = plt.gca()
minX = sys.float_info.max
maxX = -minX
minY = minX
maxY = maxX
for px, py, color, size, label in zip(x, y, colors, s,labels):
    # plot circles using the RGBA colors
    circle = plt.Circle((px, py), size, color=color, fill=False,label=label)
    ax.add_artist(circle)
    minX = min(minX, px - size)
    minY = min(minY, py - size)
    maxX = max(maxX, px + size)
    maxY = max(maxY, py + size)

plt.xlim([minX, maxX])
plt.ylim([minY, maxY])
ax.set_aspect(1.0)  # make aspect ratio square

# plot the scatter plot
plt.scatter(x, y, s=0, c=c, cmap='jet', facecolors='none')
plt.grid()
plt.colorbar()  # this works because of the scatter
plt.show()
