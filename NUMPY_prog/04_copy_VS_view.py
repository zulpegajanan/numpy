import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("x=",x)
print("\n\ncopy of x with modification",arr)
print("after coping x=",x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print("\n\nview of x with modification =",arr)
print("after modification of in view",x)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print("base of copy array",x.base)
print("base of view array",y.base)
