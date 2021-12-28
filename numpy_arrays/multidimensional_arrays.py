import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([
    [
        [10, 20, 30, 40], [8, 8, 2, 1], [1, 1, 1, 2]
    ],
    [
        [9, 9, 2, 39], [1, 2, 3, 3], [0, 0, 3, 2]
    ],
    [
        [12, 33, 22, 1], [22, 1, 22, 2], [0, 2, 3, 1]
    ]
], dtype=float)

# this creates a 2x3 matrix.
print(a)
print(b)
# Since we now have two dimensions, we also need to address two indices, in
# order to access a specific element.
print(a[1][2])
