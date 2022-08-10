import numpy as np

int_arr = np.array([1, 2, 3, 4])
print(int_arr.dtype)

str_arr = np.array(['apple', 'banana', 'cherry'])
print(str_arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print("int arr to string arr ",arr)
print(arr.dtype)
#A non integer string like 'a' can not be converted to integer (will raise an error):
#A non integer string like 'a' can not be converted to integer (will raise an error):
#A non integer string like 'a' can not be converted to integer (will raise an error):

#Converting Data Type on Existing Arrays


#float to integer conversion
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i') #or  newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#interger to boolean
print("interger to boolean conversion \n")
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
