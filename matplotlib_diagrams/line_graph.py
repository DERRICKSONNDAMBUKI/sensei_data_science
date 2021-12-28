import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 20, 100)
# Here we create an array with 100 values between 0 and 20.
y_values = np.sin(x_values)

plt.plot(x_values,y_values)
plt.show()
