import numpy as np
import matplotlib.pyplot as plt

numbers = 10*np.random.random(100)
plt.plot(numbers,'b*')
# second parameter ‘bo’ ,
# where the first letter indicates the color (blue) and the second one the shape
# (stars).
plt.show()