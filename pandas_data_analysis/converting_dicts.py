# Since series and dictionaries are quite similar, we can easily convert our
# Python dictionaries into Pandas series.
import pandas as pd

mydict = {'A':10,'B':20,'C':30}
series = pd.Series(mydict)
print(series)
# to change the order of the indice
series0=pd.Series(mydict,index=['C','A','B'])
print(series0)