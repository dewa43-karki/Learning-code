# Creating a Numpy array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print(np.__version__)



# Dimensions in Arrays
import numpy as np

# Creating a 0-D array with value 44
arr = np.array(44)

print(arr)

# Creating a 1-D array with value 44, 33, 1, 3
arr = np.array([44, 33, 1, 3])

print(arr)

# Creating a 2-D array with value 1, 3, 33 and 63, 55, 16
arr = np.array([[33, 3, 1], [16, 63, 55]])

print(arr)

# Creating a 3-D array with value 1, 3, 33 and 63, 55, 16 and 4, 81, 22
arr = np.array([[1, 3, 33], [16, 55, 63], [4, 81, 22]])

print(arr)

# Checking how many dimensions the array have
b = np.array(33)

# Creating an array with 5 dimensions and verifying that it has 5 dimensions
arr = np.array([3, 1, 33, 4, 55, 63], ndmin = 6)

print(arr)

print("Number of Dimensions : ", arr.ndim)



# NumPy Array Indexing
import numpy as np

# Getting the first element from the following array
arr = np.array([1, 2, 3, 4])

print(arr[0])

# Getting third and fourth elements from the following array and add them
print(arr[2] + arr[3])

# Accessing the element on the from the 2-D array
arr = np.array([[1, 3, 33], [16, 55, 63]])

print("Georgeee : ", arr[1, 2])

# Accessing the element on the from the 3-D array
arr = np.array([[[1, 3, 33], [16, 55, 63]], [[4, 81, 22], [7, 11, 23]]])

print(arr[0, 0, 2])

# Accessing an array from the end
arr = np.array([[1, 3, 33], [16, 55, 63]])

print("Last element from 2nd dim : ", arr[1, -1])



# NumPy Array Slicing
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slicing elements from index 1 to index 5
print(arr[1:5])

# Slicing elements from index 4 to the end of the array
print(arr[4:])

# Slicing elements from the beginning to index 4 (not included)
print(arr[:4])

# Slicing from the index 3 from the end to index 1 from the end
print(arr[-3:-1])

# Returning every other element from index 1 to index 5
print(arr[1: 5: 2])

# Returning every other element from the entire array
print(arr[::2])

# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Slicing elements from index 1 to index 4 (not included)
print(arr[1, 1:4])

# From both elements, returning index 2
print(arr[0:2, 2])

# From both elements, slicing index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])



# NumPy Data Types
import numpy as np

# Geting the data type of an array object
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Geting the data type of an array containing strings
arr = np.array(['watermelon', 'orange', 'mango', 'guava'])
print(arr.dtype)

# Creating Arrays With a Defined Data Type

# Creating an array with data type string
arr = np.array([1, 2, 3, 4], dtype = 'S')
print(arr)
print(arr.dtype)

# Creating an array with data type 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype = 'i4')
print(arr)
print(arr.dtype)
