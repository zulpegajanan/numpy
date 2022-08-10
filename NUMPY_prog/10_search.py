import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("arr is=",arr)
x = np.where(arr == 4)
print("index where value is 4 =>",x)

print("Find the indexes where the values are even:")
x = np.where(arr%2 == 0)
print("even value at index in arr",x)
