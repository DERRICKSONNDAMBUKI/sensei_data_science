import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Anna', 'Bob', 'Charles',
                 'Daniel', 'Evan', 'Fiona',
                 'Gerald', 'Henry', 'India'],
        'Age': [24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height': [176, 187, 175, 182, 176,
                   189, 165, 187, 167]}
df = pd.DataFrame(data)
df.sort_values(by=['Age','Height'])

# histogram
# df.hist()

# line graph
# df.plot()

# star plot
plt.plot(df['Age'],'b*')
plt.show()