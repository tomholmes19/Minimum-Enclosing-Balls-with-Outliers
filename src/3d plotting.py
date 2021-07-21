import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

import data.generation

fig = plt.figure()
ax = Axes3D(fig)

data = data.generation.two_clusters(1000, 3, 0.9, 0,1, 4,1)

x_vals = data[:,0]
y_vals = data[:,1]
z_vals = data[:,2]

ax.scatter(x_vals, y_vals, z_vals, alpha=0.5)
plt.show()