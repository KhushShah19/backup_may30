
# why numpy over list??
# much faster and takes very less space compare to list
# also we can make 2D and 3D arrays

import numpy as np

# c = np.arange(15).reshape(3, 5)
# print(c)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([[1, 3, 5], [2, 9, 6]])

print("array a :", a)
print()
print("array b :", b)
print()
print("dimension of array a :", a.ndim, "(just int)") # to know the dimension of a : (just int)
print("to know the dimension of array b :", b.ndim, "(just int)")
print()
print('shape of array a :', a.shape, "[Rows Only cause one dimension]") # to know the shape of a  
print("to know the shape of array b :", b.shape, "(rows, coloum)")
print()
print("size of array a :", a.dtype, "(in int = 4*bites)") # to know the size of array a
print("size of array a :", a.itemsize, "(in bites)") # to know the size of array a 
print("number of items in array a :", a.size) # number of items in it























