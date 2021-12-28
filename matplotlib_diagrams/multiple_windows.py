import numpy as np
import matplotlib.pyplot as plt

# subplots These are plots that are shown in the same window but independently from each other.

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

plt.figure(1)
plt.plot(x, y1, 'r-')
# r- is for coloring

plt.figure(2)
plt.plot(x, y2, 'g--')

plt.show()
# By doing this, we can show two windows with their graphs at the same time.
# Also, we can use subplots within figures.