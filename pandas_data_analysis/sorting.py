import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 2), index=[
                  1, 5, 3, 6, 7, 2, 8, 9, 0, 4], columns=['A', 'B'])
print(df)
print('sorted list: \n', df.sort_index())
# The alternative is the parameter inplace parameter . When this parameter is set to True , the changes get
# applied to our actual data frame.

data = {'Name': ['Anna', 'Bob', 'Charles',
                 'Daniel', 'Evan', 'Fiona',
                 'Gerald', 'Henry', 'India'],
        'Age': [24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height': [176, 187, 175, 182, 176,
                   189, 165, 187, 167]}
df = pd.DataFrame(data)
print('\n',df)
df.sort_values(by=['Age','Height'],inplace=True)
print('\nSorted by Age and Height:\n',df)
# We use the function sort_values to sort our data frames. The parameter by states the columns that
# we are sorting by. In this case, we are first sorting by age and if two persons
# have the same age, we sort by height.