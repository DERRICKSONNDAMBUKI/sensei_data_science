import pandas as pd

data = {
    'Name':['Anna','Ricky','Sensei','Rube','Joy','Lilliana','Grace','Ian','Summer'],
    'Age':[24,32,35,45,22,54,55,43,25],
    'Height':[175,187,175,182,176,189,165,187,167]
}
df = pd.DataFrame(data=data)

print(df.loc[df['Age']==24])

# print(df.loc[(df['Age']==24)&(df['Height']>180)])
print('\n',df.loc[df['Age']>30]['Name'])