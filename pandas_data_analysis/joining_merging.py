import pandas as pd

names = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Anna', 'Bob', 'Charles',
             'Daniel', 'Evan'],
})
ages = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'age': [20, 30, 40, 50, 60]
})
# It is important that we have a common column that we can merge on. In this case, this is id
df = pd.merge(names, ages,on='id')
df.set_index('id',inplace=True)
print(df)