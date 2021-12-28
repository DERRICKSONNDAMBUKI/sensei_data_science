# It provides high-performance tools for data manipulation and analysis. Furthermore, it is very
# effective at converting data formats and querying data out of databases. The
# two main data structures of Pandas are the series and the data frame.
import pandas as pd

# A series in Pandas is a one-dimensional array which is labeled.
series = pd.Series([10,20,30,40],
                   ['A','B','C','D'])
# The first parameter that we pass is a list full of values (in this case numbers). The
# second parameter is the list of the indices or keys (in this case strings).
print(series)
# The first column represents the indices, whereas the second column represents
# the actual values.

# accessing values
print(series['C'])
print(series[1]) # We can either address the key or the position that the respective element is at.
