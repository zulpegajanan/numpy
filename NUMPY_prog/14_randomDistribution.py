from numpy import random
print("Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.\nThe probability for the value to be 3 is set to be 0.1\nThe probability for the value to be 5 is set to be 0.3\nThe probability for the value to be 7 is set to be 0.6\nThe probability for the value to be 9 is set to be 0\n\n")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print("random generated array is\n",x)