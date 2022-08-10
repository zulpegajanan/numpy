#ufuncs stands for "Universal Functions"
import numpy as np

print("addition of two list")
list1=[1,2,3,4]
list2=[5,6,7,8]
print(list1)
print(list2)
newlist=[]

print("\nusing zip()")
for i, j in zip(list1, list2):
  newlist.append(i + j)
print(newlist)

print("\nusing add()")
newlist = np.add(list1, list2)
print(newlist)