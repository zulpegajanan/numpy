# Python program to demonstrate
# basic array characteristics
import numpy as np
 
#checking numpy version
print("the version of numpy  is ",np.__version__)

# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
#Printing array
print("array is ",arr)

# Printing type of arr object
print("Array is of type: ", type(arr))
 
# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
 
# Printing shape of array
print("Shape of array: ", arr.shape)
 
# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
 
 #0-D array
a = np.array(42)
print("for zero dircn array",a.ndim)

#1-D array
b = np.array([1, 2, 3, 4, 5])
print("for one dircn array",b.ndim)
print("in 1D element at index 1 is",b[1])
#2-D array
c = np.array([[1, 2, 3], [4, 5, 6]])
print("for two dircn array",c.ndim)
print('2nd element on 1st row: ', c[0, 1])
#3-D array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("for three dircn array",d.ndim)
print((arr[0, 1, 2]))
#HIGHER DIMENSION
#Create an array with 5 dimensions and verify that it has 5 dimensions:
arr_size5 = np.array([1, 2, 3, 4], ndmin=5)
print("for array of dimension 5 ",arr_size5)
print('number of dimensions :', arr_size5.ndim)
