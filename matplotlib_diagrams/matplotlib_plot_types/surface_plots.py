import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')


def z_function(x, y):
    return np.sin(np.sqrt(x**2+y**2))


x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
# We start by defining a z_function which is a combination of sine, square root
# and squaring the input. Our inputs are just 50 numbers from -5 to 5
X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)
ax.plot_surface(X, Y, Z)
plt.show()
