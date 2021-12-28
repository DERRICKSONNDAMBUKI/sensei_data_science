import pandas as pd

# In contrast to the series, a data frame is not one-dimensional but multi-
# dimensional and looks like a table. You can imagine it to be like an Excel
# table or a data base table.

data = {
    'Name':['Anna','Ricky','Sensei'],
    'Age':[17,15,18],
    'Height':[176,187,175]
    }
df= pd.DataFrame(data)
print(df)
# accessing values
print('\n\n',df[['Name','Height']])
