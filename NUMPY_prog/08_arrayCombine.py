import numpy as np

arr1 = np.array([1, 2, 3])
print("arr1=",arr1)
arr2 = np.array([4, 5, 6])
print("arr2=",arr2)

print("using concatenate()")
arr = np.concatenate((arr1, arr2))
print(arr)

print("using stack")
arr = np.stack((arr1, arr2), axis=1)
print(arr)

print("using stack along row i.e. hstack()")
arr = np.hstack((arr1, arr2))
print(arr)

print("using stack along columns i.e. vstack()")
arr = np.vstack((arr1, arr2))
print(arr)

print("using stack along height or depth i.e. dstack()")
arr = np.vstack((arr1, arr2))
print(arr)
