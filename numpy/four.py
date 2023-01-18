import numpy as np 

arr1 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr1)

arr2 = np.array([1,2,3,4,5,6])
arr3 = np.reshape(arr2, (3,2))
print(arr3)

print(np.zeros((3,2)))
print(arr1.flatten())

