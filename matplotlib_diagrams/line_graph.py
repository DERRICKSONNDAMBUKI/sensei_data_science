import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 20, 100)
y_values = np.sin(x_values)

plt.plot(x_values,y_values)
plt.show()
