### Numpy
The NumPy module allows us to efficiently work with vectors, matrices and multi-dimensional arrays. It is crucial for linear algebra and numerical analysis.

### Scipy
NumPy is basically just managing the arrays and lists. It is responsible for the operations like indexing, sorting, slicing, reshaping and so on. Now, SciPy actually uses NumPy to offer more abstract classes and functions that solve scientific problems.

### Matplotlib
This library is responsible for plotting graphs and visualizing our data. It offers numerous types of plotting, styles and graphs.

Visualization is a key step in data science.

### Pandas
It offers us a powerful data structure named data frame . You can imagine it to be a bit like a mix of an Excel table and an SQL database table.

### Libraries needed in Data science
pip install numpy
pip install scipy (optional)
pip install matplotlib
pip install pandas

NUMPY ARRAY ATTRIBUTES
ATTRIBUTE   DESCRIPTION
a.shape     Returns the shape of the array
            e.g. (3,3) or (3,4,7)

a.ndim      Returns how many dimensions our
            array has

a.size      Returns the amount of elements an
            array has

a.dtype     Returns the data type of the values in
            the array

NUMPY MATHEMATICAL FUNCTIONS
FUNCTION    DESCRIPTION
np.exp(a)   Takes e to the power of each value
np.sin(a)   Returns the sine of each value
np.cos(a)   Returns the cosine of each value
np.tan(a)   Returns the tangent of each value
np.log(a)   Returns the logarithm of each value
np.sqrt(a)  Returns the square root of each value

NUMPY AGGREGATE FUNCTIONS
FUNCTION    DESCRIPTION
a.sum()     Returns the sum of all values in the
            array
a.min()     Returns the lowest value of the array
a.max()     Returns the highest value of the array
a.mean()    Returns the arithmetic mean of all
            values in the array
np.median(a)Returns the median value of the array
np.std(a)   Returns the standard deviation of the
            values in the array

SHAPE MANIPULATION FUNCTIONS
FUNCTION        DESCRIPTION
a.reshape(x,y)  Returns an array with the same
                values structured in a different shape
a.flatten()     Returns a flattened one-dimensional
                copy of the array
a.ravel()       Does the same as flatten but works
                with the actual array instead of a
                copy
a.transpose()   Returns an array with the same
                values but swapped dimensions
a.swapaxes()    Returns an array with the same
                values but two swapped axes
a.flat          Not a function but an iterator for the
                flattened version of the array

for x in a.flat:
    print (x)
print (a.flat[ 5 ])

#          JOINING FUNCTIONS
FUNCTION            DESCRIPTION
np.concatenate(a,b) Joins multiple arrays along an
                    existing axis
np.stack(a,b)       Joins multiple arrays along a
                    new axis
np.hstack(a,b)      Stacks the arrays horizontally
                    (column-wise)
np.vstack(a,b)      Stacks the arrays vertically
                    (row-wise)

SPLITTING FUNCTIONS
FUNCTION        DESCRIPTION
np.split(a, x)  Splits one array into multiple
                arrays
np.hsplit(a, x) Splits one array into multiple
                arrays horizontally (column-wise)
np.vsplit(a, x) Splits one array into multiple 
                arrays vertically (row-wise)

ADDING AND REMOVING FUNCTIONS
FUNCTION            DESCRIPTION
np.resize(a, (x,y)) Returns a resized version of the
                    array and fills empty spaces by
                    repeating copies of a
np.append(a, [...]) Appends values at the end of the
                    array
np.insert(a, x, ...)Insert a value at the index x of the
                    array
np.delete(a, x, y)  Delete axes of the array

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
