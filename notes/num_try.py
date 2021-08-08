
"""# why numpy over list??
# much faster and takes very less space compare to list
# also we can make 2D and 3D arrays (any matrix)
# also more opertation, easy changes, easy extraction"""

import numpy as np  # NumPy Documentation -- https://numpy.org/doc/

# c = np.arange(15).reshape(3, 5)
# print(c)
NUMP = 1001
timepass = 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([[1, 3, 5], [2, 9, 6]])

if NUMP == 10: # About array(shape, size, etc)
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
    print("total size of array a :", a.size*a.itemsize, "(in bites)")
    print("a.size*a.itemsize = a.nbytes =", a.nbytes) # both are same

elif NUMP == 20: # Slicing or Extractation
    print("to get 9 from array b (1row, 1coloum):", b[1,1]) # rows and coloum also starts from 0
    print("a[1, 1] = a[-1, -2] =", b[-1, -2]) # same as in list
    print("to get 2nd row :", b[1, : ])
    print("to get 1st coloum :", b[:, 0])
    print("slicing to get 9 (startindex, endindex, stepsize):", b[1, 1:2:3]) # stepsize = number of gaps

elif NUMP == 30: # changing the elements of b (bigger to smaller = outer to inwards)
    b[1, -1] = 11 # changing a specific element
    b[:, 0] = 0 # changing the complete ROW to 0
    b[:, 0] = [2, 7]
    b[1, :] = [7, 11, 13]
    print( b, "= new b") # [[2, 3, 5], [7, 11, 13]]

elif NUMP == 40: # Initialization Different Types of Arrays
    # last two (...m, n) => ... rows, coloum (fixed)
    z = np.zeros((2, 3, 4, 6)) # 2 sets of 3 martics with 4 rows and 6 coloums with All Zeros
    y = np.ones((1, 2, 3), dtype="int32") # All one

    x = np.full((2, 3), 99)
    x1 = np.full_like(b, 7)
    x2 = np.full(b.shape, 7)
    print(x, x1, x2) # all same

    #print(z, y)
    #print(type(y[0, 0]), type(b[0, 0]))
    p = np.ndarray((2, 3))
 
    # z, y, x, w, v, u, t, s, r, q, p

    w = np.random.rand(2, 3) # random decimals (0<w<1) values

    v = np.random.randint(2, 8, size=(3,4)) # random int (2<=v<8) values

    u = np.identity(5) # identity square matrix (digonals = 1 and other all = 0)

    t = np.array([[7, 9, 5]])
    t1 = np.repeat(t, 3, axis=1) # t1 = [[7 7 7 9 9 9 5 5 5]]
    t2 = np.repeat(t, 3, axis=0) # t2 = repeat t, 3 times
    print(t, t1, t2)

elif NUMP == 50: # Basic Mathematics
    e = np.array([2, 4, 6, 8])
    print(e+2, e/2, e**2, np.sin(e))
    print(e > 5, e[e > 5], e[[0, 1]])

    f = np.array([3, 5, 7, 9])
    print(e+f) # same size

elif NUMP == 60: # Linear Algebra and Statistics
    # Linear Algebra -- https://numpy.org/doc/stable/reference/routines.linalg.html

    g = np.ones([3, 4], dtype="int32")
    h = np.full([4,3], 5, dtype="int32")

    gh = np.matmul(g, h)
    gh_det = np.linalg.det(gh)

    # Statistics

    e = np.array([2, 4, 6, 8])
    print(np.min(e), np.max(h, axis=1), np.sum(e))

elif NUMP == 70: # Reorganization, Copy and adding arrays

    # Reorganization of Arrays

    i = b.reshape([2, 4])
    print(i)


    # stacking vectors(adding two arrays)

    j = np.array([2, 4, 6, 8], dtype="int32") 
    k = np.array([3, 5, 7, 9], dtype="int32")

    jk = np.vstack([j, k, j]) # vstack = vertically stack
    jk_0 = np.hstack([j, k]) # hstack = horizatically stack

    print(jk_0)

    # COPY (CareFull.... )
    d = np.array([3, 4, 5])
    d1 = d # now changes will be made to both cause it's not COPY    
    d2 = d.copy() # now this is copy

elif NUMP == 99: # load data from file

    m = np.genfromtxt("sd01")
    print(m)

if NUMP == 1000 : # Questions
    q1 = np.ones([5, 5], dtype="int32")
    q1[1, 1:4] = 0
    q1[2, 1:4] = 0
    q1[3, 1:4] = 0
    q1[2, 2] = 9 #.....done

    q11 = np.ones([5, 5], dtype="int32")
    q1_1 = np.zeros([3, 3], dtype="int32")
    q1_1[1, 1] = 9
    q11[1:4, 1:4] = q1_1 # .....another way

    print(q11)

print("End")
