import numpy as np
import matplotlib.pyplot as plt

x= np.random.rand(50)
y= np.random.rand(50)
# we just generate 50 random x-values and 50 random y-values.
plt.scatter(x, y)
plt.show()