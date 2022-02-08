import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import *
from numpy import meshgrid
from mpl_toolkits.mplot3d import Axes3D

def schwefel( x1,x2):  
    return 418.9829*2 - x1 * sin( sqrt( abs( x1 )))-x2*sin(sqrt(abs(x2)))

x1=linspace(-500,500)
x2=linspace(-500,500)
r_min,r_max=-500,500

x1,x2=np.meshgrid(x1,x2)
results=schwefel(x1,x2)
figure=plt.figure()
axis=figure.gca(projection='3d')
axis.plot_surface(x1,x2,results, rstride=1, cstride=1, cmap=cm.jet, edgecolor='darkred', linewidth=0.1)
axis.set_xlabel('X')
axis.set_ylabel('Y')
axis.set_zlabel('Z')
plt.show()