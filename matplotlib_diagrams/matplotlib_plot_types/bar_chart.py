import numpy as np
import matplotlib.pyplot as plt

ricky = (90,67,87,76)
sensei = (80,80,47,66)
joan= (40,95,76,89)

skills=('Python','Java','Networking','Machine Learning')

width = 0.2
index = np.arange(4)
plt.bar(index, ricky,width=width,label='Ricky')
plt.bar(index +width,sensei,width=width,label='Sensei')
plt.bar(index+width*2, joan,width=width,label = 'Joan')
# we define an array
# with the indices one to four and a bar width of 0.2. For each person we plot
# the four respective values and label them.

plt.xticks(index+width,skills)
plt.ylim(0,120)
# Then we label the x-ticks with the method xticks and set the limit of the y-axis
# to 120 to free up some space for our legend.
plt.title('IT Skill Levels')
plt.ylabel('Skill Level')
plt.xlabel('IT Skill')
plt.legend()
plt.show()