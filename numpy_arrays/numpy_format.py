import numpy as np
# saving and loading arrays
a= np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [100,110,120]
])
# saving on .npy file
np.save('my_array.npy', a)
# Notice that you don’t have to use the file ending npy . use it for clarity.
# You can pick whatever you want.

# saving on .csv file
np.savetxt('my_array.csv', a)


# loading
b = np.load('./my_array.npy')

c= np.loadtxt('./my_array.csv')
print('loading from numpy format file:\n\n',b)
print('\nloading form csv file: \n\n',c)

# d = np.loadtxt( './my_array.csv' , delimiter = ';' ) # ricky has a bug
# print('\n\n',d)