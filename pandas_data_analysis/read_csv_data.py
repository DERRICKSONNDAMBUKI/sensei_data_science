import pandas as pd

df=pd.read_csv('./data.csv')
df.set_index('Age',inplace=True)
print(df)
