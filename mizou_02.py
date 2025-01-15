import numpy as np

array = np.array([[5,5,5],[5,5,5],[5,5,5]])

for l in range(array.shape[0]):
    for c in range(array.shape[1]):
        if c == 2:
            array[l,c] = 8

print(array)