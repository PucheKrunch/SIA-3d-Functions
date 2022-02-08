from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def weierstrass(x):
    sum1,sum2,sum3 =0,0,0
    a=0.5
    b=3
    kmax=20
    for i in range(1, len(x)+1):
        for k in range(0,kmax+1):
            sum2 += a**k * np.cos(2 * np.pi * b**k * (x[i-1] + 0.5))
        sum1 += sum2
    for k in range(0,kmax+1):
        sum3 += a**k * np.cos(2 * np.pi * b**k * 0.5)
    result = sum1 - (len(x) * sum3)
    return  result

#used codes from Tutorial
def plot3D(fn, xLowerBound, xUpperbound, yLowerBound, yUpperbound,name):
    X = np.linspace(xLowerBound, xUpperbound, 200)  # points in the x axis
    Y = np.linspace(yLowerBound, yUpperbound, 200)  # points in the y axis
    X, Y = np.meshgrid(X, Y)  # create meshgrid
    Z = fn([X, Y])  # Calculate Z

    # Plot the 3D surface for function from project
    fig = plt.figure(name)
    ax = fig.gca(projection='3d')  # set the 3d axes
    ax.plot_surface(
        X, Y, Z,
        rstride=1, 
        cstride=1, 
        cmap=cm.jet, 
        edgecolor='darkred', 
        linewidth=0.1
    )
    plt.title(name)
    #plt.savefig("../img/2d3D/" + name + ".png", bbox_inches='tight')
    #plt.close()
    plt.show()

plot3D(weiestrass,0,1,0,1,"Weierstrass Function")