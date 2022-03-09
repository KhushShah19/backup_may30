
# What is Machine Learning?
# the field of study that gives computers the ability to learn without being explicitly programmed.
# explicitly - in a clear and detailed manner, leaving no room for confusion or doubt.
# basically letting machine learn who to copy humans and do things better than humans

# mainly ML is of two types -- A. Supervised learning and B. Unsupervised learning
ML = 0
timepass = 1
import numpy as np

if ML == 10: # Supervised learning(SL) ML

    # in SL, we are given a data set and already know what our correct output should look like
    # Supervised learning problems are categorized into "regression" and "classification" problems.
    # basicaaly callification - which have options, regression - without options
    pass

elif ML == 20: # UnSupervised learning(SL) ML

    # data without any labells(names), USL helps to related/patter them
    # mainly two categore "Clustering" and "Non Clustering"
    # Non Clustering: data mix(overlap) with each other, Clustering: Non mix data
    pass

elif ML == 30: # Linear regression with one variable (Modle representation)
    # a graph of (home area size(x-axis)) and (cost of that home(y-axis))

    i = 0  
    m = "number of training set OR number of set of (x,y) given"
    x = "input variable / features" # NOTATION
    y = "output variable / traget varable"
    (x, y) = "one training set"
    (x[i], y[i]) = "i-th training set"

    # Training set -> Learning Algorithm -> h(Hypothesis)
    # h -- it takes (x-axis) value and pridect (y-axis) value 
    c = "Constant" # Gradient Descent (best way to deal Hypothesis-prameters)
    h = m*x + c # Linear -- Stringht line 
    # we are learning how to choose the value of m and c (m, c = Parameters)
    # Hint: (m, c) is choose such that h(= m*x +c) is close to y in our set (x, y)
    def cost(x, y, m): 
        l = []
        for i in range: # here l = a quadratic(2nd degree) graph 
            l = l + [((h(x(i)) - y(i))^2)/2*m]
        J = min(l) # here we find the golbal minuimum point of graph

    
elif ML == 1000: # Gradient Descent (best way to deal Hypothesis-prameters)
    # Training set -> Learning Algorithm -> h(Hypothesis)
    # h = mx + c (Linear => Stringht line)  
    # h(Hypothesis), m(Slope)and c(Constant) all three are parameters
    import numpy as np 
    # learning to choose the value of "m" And "c" To Get "h" And pridect "y" 

    x = np.array([2, 4, 6, 8, 10]) # two random set
    y = np.array([3.2, 5.4, 7.2, 9.3, 11.8])

    def fun(x, y): # given two lists and pridecting values(if not given)
        m, c = 0, 0 # assuming some random values
        n = len(x) # assuming lenght of both the list as equal
        times = 1000 # number of times to run(Iteration)
        learning_rate = 0.0218999 # moves it takes as it move towards globle minumum
        phone = 0
        for i in range(times):
            h = m*x + c # h = mx + c (Linear => Stringht line)  
            mrp = (1/n)*sum([val**2 for val in (h-y)]) # main formula of 
            j = (1/n)*sum((h-y)**2) # j == mrp (same)
            dm = (2/n)*sum((h-y)*x) # differentation wrt m and then adding them
            dc = (2/n)*sum(h-y) # differentation wrt c and then adding them
            # differentation also tells where to go(with help of sign)
            m = m - (learning_rate*(dm)) # decreasing it with some rate
            c = c - (learning_rate*(dc)) # at some point it will become zero
            # print(i, m, " ", c, " ", mrp)
        
        return "Done"
    print(fun(x, y))    

elif ML == 1100: # if (c, m) is know then best way is matrix product
    x_values = [2, 4, 6, 8] # given "x" value for which "y" values are to be find
    x_array = np.array(x_values) # making it array
    x_matrix = np.ones((4, 2), dtype="int32") 
    x_matrix[:, 1] = x_array # making it matrix

    if timepass == 0: # if Only One (c, m)
        c1m1_values = [2, 2] # [c, m] given
        c1m1 = np.array(c1m1_values) # making it array
        cmv1 = c1m1.reshape([2, 1]) # making it matrix
        xcm1 = np.dot(x_matrix, cmv1) # product of them(dot)
        print(xcm1)

    if  timepass == 1: # if more then One(for example 3)
        c3m3_values = [[2, 2], [2, 1.9], [2, 2.1]] # given as list
        c3m3 = np.array(c3m3_values) # making it array
        cmv3 = np.zeros((2, 3), dtype=float)
        for i in range(3):
            cmv3[:, (i-1)] = c3m3[i-1] # making it matrix
        xcm3 = np.dot(x_matrix, cmv3) # product of them(dot)
        print(xcm3)


bbb = 10 
bbb = 10 + bbb

print("End")
 

