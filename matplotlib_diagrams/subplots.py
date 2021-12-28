import numpy as np
import matplotlib.pyplot as plt

# subplots These are plots that are shown in the same window but independently from each other.

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

plt.subplot(211)
# The parameter we pass defines the grid of our window.
# The first digit indicates the number of rows, the second the number of
# columns and the last one the index of the subplot. So in this case, we have
# two rows and one column. Index one means that the respective subplot will be
# at the top.
plt.plot(x, y1, 'r-')
# r- is for coloring

plt.subplot(212)
plt.plot(x, y2, 'g--')


plt.show()
