import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("original 1D array is ",arr)

newarr = arr.reshape(4, 3)
print("one array of collection of  4 1D array with each having 3 element ",newarr)

newarr = arr.reshape(2, 3, 2)
print("2 array with combinaton of 3 1D array each having 2 element each\n",newarr)
