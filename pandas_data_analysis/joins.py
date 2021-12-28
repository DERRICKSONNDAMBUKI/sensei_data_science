import pandas as pd

names = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Anna', 'Bob', 'Charles',
             'Daniel', 'Evan', 'Fiona'],
})
ages = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 7],
    'age': [20, 30, 40, 50, 60, 70]
})

# df = pd.merge(names, ages,on='id',how='inner')
# If we now perform the default inner join , we will end up with the same data
# frame as in the beginning. We only take the keys which both objects have.
# This means one to five.

# df = pd.merge(names, ages,on='id',how='left')
# When we use the left join , we get all the keys from the names data frame but
# not the additional index 7 from ages. This also means that Fiona won’t be
# assigned any age.

# The same principle goes for the right join just the other way around.
# df = pd.merge(names, ages,on='id',how='right')

# Now, we only have the keys from the ages frame and the 6 is missing.
# Finally, if we use the outer join , we combine all keys into one data frame.
df = pd.merge(names, ages,on='id',how='outer')

df.set_index('id',inplace=True)
print(df)