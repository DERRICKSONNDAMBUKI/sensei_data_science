from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt

style.use('ggplot')
# Here we apply the style of ggplot . This adds a grid and
# some other design changes to our plots. For more information, check out the
# link here https://bit.ly/2JfhJ4o

plt.figure('Sensei figure')
plt.title('Sine Function')
plt.suptitle('Data Science') # adds an additional centered title above the first title

# label the axes
plt.xlabel('100 values between 0-50')
x= np.linspace(0,50, 100)  
plt.ylabel('sine of x values')
y1=np.sin(x)
y2=np.cos(x)
y3= np.log(x/3)

plt.grid(True)
plt.plot(x,y1,'b-',label='Sine')
plt.plot(x,y2,'r-',label='Cosine')
plt.plot(x,y3,'g-',label='Logarithm')
plt.legend(loc='upper left')
plt.savefig('functions.png')
plt.show()
