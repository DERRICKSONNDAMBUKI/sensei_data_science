import numpy as np
import matplotlib.pyplot as plt

labels = ('Nakuru City','Nairobi City','Mombasa City','Other')
values =(47,23,20,10) # adds up to 100%

plt.pie(values,labels=labels,autopct='%.2f%%',shadow=True)
# set the autopct parameter to our desired percentage format
plt.title('Student Nationalities')
plt.show()

