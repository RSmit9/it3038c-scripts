import numpy as np

array1 = np.arange(10)

array2 = np.reshape(np.arange(10), (2, 5))

print("array 1:", arr1)
print("array 2:", arr2)

array2 -= 20

array1 *= 10

print("array 1 after manipulation:", arr1)
print("array 2 after manipulation:", arr2)
