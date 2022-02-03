import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def EggHolder(x):
    x1, x2 = x
    return -(x2+47)*np.sin(np.sqrt(np.abs(x2+(x1/2)+47)))-x1*np.sin(np.sqrt(np.abs(x1-(x2+47))))

fig = plt.figure()
ax = fig.gca(projection='3d')
X1 = X2 = np.arange(-512, 513, 1)
X1, X2 = np.meshgrid(X1, X2)
F = EggHolder((X1, X2))
surface = ax.plot_surface(X1, X2, F, linewidth=0, antialiased=False)

ax.set_zlim(-1000, 1000)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surface, shrink=0.5, aspect=5)
plt.show()