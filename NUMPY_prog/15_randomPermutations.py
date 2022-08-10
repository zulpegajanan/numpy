from numpy import random
import numpy as np
print("The NumPy Random module provides two methods for this: shuffle() and permutation().")

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("using suffle()")
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print("using permutation()")
print(random.permutation(arr))