import pandas as pd
import numpy as np

data = {
    'Name':['Anna','Ricky','Sensei','Rube','Joy','Lilliana','Grace','Ian','Summer'],
    'Age':[24,32,35,45,22,54,55,43,25],
    'Height':[175,187,175,182,176,189,165,187,167]
}
df = pd.DataFrame(data=data)
print(df)
# print('mean: ',df.mean()) # returns mean for each column
print('\nmean: ',df['Age'].mean())
print('meadian: ',df['Height'].median())

# applying numpy functions
print('\nsine of age: \n',df['Age'].apply(np.sin))

# labda expressions
print('using lambda: \n',df['Age'].apply(
    lambda x : x*100
))
# using the keyword lambda we create a temporary variable that represents
# the individual values that we are applying the operation onto. After the colon,
# we define what we want to do. In this case, we multiply all values of the
# column Age by 100.

data0=df[['Age','Height']]
print('\n',data0.apply(
    lambda x : x.max()-x.min()
)) # The oldest and the youngest are 33 years apart and the tallest and the tiniest
# are 24 centimeters apart.

# iterating
for x in df['Age']:
    print(x)

for key,value in df.iteritems():
    print('\n{}:\n{}'.format(key,value))
    # iteritems function to iterate over key-value pairs. all rows for each column.
for index,value in df.iterrows():
    print(index,value)  # iterrows , we can print out all the column-
                        # values for each row or index.