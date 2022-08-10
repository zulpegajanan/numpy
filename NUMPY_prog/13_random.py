from numpy import random
import numpy as np

print("\nGenerate a random integer from 0 to 100:")
x = random.randint(100)
print(x)

print("\nrandom float between 0 and 1.")
x = random.rand()
print(x)

print("\nGenerate a 1-D array containing 5 random integers from 0 to 100:")
x=random.randint(100, size=(5))
print(x)

print("\nGenerate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:")
x = random.randint(100, size=(3, 5))
print(x)

print("\nGenerate a 2-D array with 3 rows, each row containing 5 random numbers:")
x = random.rand(3, 5)
print(x)

arr=np.array([3,5,7,9])
x = random.choice([3, 5, 7, 9])
print("\n\narray is ",arr)
print("random element of this array is ",x)
