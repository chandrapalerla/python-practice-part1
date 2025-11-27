import numpy as np

# Create a 1-dimensional array (vector)
a = np.array([1, 2, 3, 4, 5])
print("1D Array 'a':", a)
print("Shape of 'a':", a.shape) # Output: (5,)

# Create a 2-dimensional array (matrix)
# This is a 3x3 matrix (3 rows, 3 columns)
b = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
print("\n2D Array 'b':\n", b)
print("Shape of 'b':", b.shape) # Output: (3, 3)

# Creating arrays of zeros or ones is common
c = np.zeros((2, 4)) # A 2x4 array filled with zeros
print("\nArray 'c' (zeros):\n", c)