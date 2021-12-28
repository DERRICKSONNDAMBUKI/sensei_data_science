# BASIC FUNCTIONS AND ATTRIBUTES
FUNCTION    DESCRIPTION
df.T        Transposes the rows and columns of
            the data frame
df.dtypes   Returns data types of the data frame
df.ndim     Returns the number of dimensions of
            the data frame            
df.shape    Returns the shape of the data frame
df.size     Returns the number of elements in
            the data frame
df.head(n)  Returns the first n rows of the data
            frame (default is five)
df.tail(n)  Returns the last n rows of the data
            frame (default is five)

# STATISTICAL FUNCTIONS
FUNCTION    DESCRIPTION
count()     Count the number of non-null
            elements
sum()       Returns the sum of values of the
            selected columns
mean()      Returns the arithmetic mean of
            values of the selected columns
median()    Returns the median of values of the
            selected columns
mode()      Returns the value that occurs most
            often in the columns selected
std()       Returns standard deviation of the
            values
min()       Returns the minimum value
max()       Returns the maximum value
abs()       Returns the absolute values of the
            elements
prod()      Returns the product of the selected
            elements
describe()  Returns data frame with all statistical
            values summarized
iteritems() Iterator for key-value pairs
iterrows()  Iterator for the rows (index, series)
itertuples()Iterator for the rows as named tuples

# JOIN MERGE TYPES
JOIN    DESCRIPTION
left    Uses all keys from left object and
        merges with right
right   Uses all keys from right object and
        merges with left
outer   Uses all keys from both objects and
        merges them
inner   Uses only the keys which both
        objects have and merges them
        (default)

## Quering Data
Like in databases with SQL, we can also query data from our data frames in Pandas. For this, we use the function loc , in which we put our expression.