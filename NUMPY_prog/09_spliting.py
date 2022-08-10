import numpy as np
print("spliting with 1D array")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(arr)
print(newarr[0])
print(newarr[1])
print(newarr[2])


print("\n\n spliting with 2D array")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)

print("\nSplit the 2-D array into three 2-D arrays.\n")
newarr = np.array_split(arr, 3)
print(newarr)

print("Split the 2-D array into three 2-D arrays along rows.")
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

print("\nusing hsplit()")
newarr = np.hsplit(arr, 3)
print(newarr)

print("\nusing vsplit()")
newarr = np.vsplit(arr, 3)
print(newarr)

# dsplit only work with 3 or more dimension
# print("\nusing dsplit()")
# newarr = np.dsplit(arr, 3)
# print(newarr)
