import numpy as np
#shape return tupple 
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)#output (dimension,no_of_ele_in_one_direction)
#(2,4)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
#shape of array : (1, 1, 1, 1, 4)

