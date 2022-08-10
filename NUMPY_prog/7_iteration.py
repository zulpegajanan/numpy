import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nusing multiple for loop")
for x in arr:
  for y in x:
    for z in y:
      print(z)

print("\nusing single for loop")
for x in arr:
  print(x)

print("\nusing nditer() function ")
for x in np.nditer(arr):
  print(x)