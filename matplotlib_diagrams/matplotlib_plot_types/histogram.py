import numpy as np
import matplotlib.pyplot as plt

mu,sigma = 172,4
x = mu+sigma*np.random.randn(1000)
# We start by defining a mean value mu (average height) and a standard
# deviation sigma . To create our x-values, we use our mu and sigma combined
# with 10000 randomly generated values. Notice that we are using the randn
# function here. This function generates values for a standard normal
# distribution , which means that we will get a bell curve of values.

plt.hist(x,100,density=True,facecolor = 'blue')
# The second parameter states how many values we want to plot. Also, we want our values
# to be normed. So we set the parameter density to True . This means that our y-
# values will sum up to one and we can view them as percentages. Last but not
# least, we set the color to blue.
plt.xlabel('Height')
plt.ylabel('Probability')
plt.title('Heights of students')
plt.text(160, 0.125, 'mu=172,sigma=4')
plt.axis([155,190,0,0.15])
plt.grid(True)
plt.show()
# 