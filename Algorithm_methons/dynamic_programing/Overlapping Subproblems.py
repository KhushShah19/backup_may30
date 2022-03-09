""" DP(Dynamic Progamming) - OVERLAPPING Sub-problem
DP divide the problem into series of Overlapping sub-problems.

We divide the problem into sub-problem which might have repeative sub-problems,
so we store the value in a table to avoid solving it again and again.

FEATURES:
    A. OVERLAPPING Sub-problem 
    B. OPTIMAL Sub-problem 

A. OVERLAPPING Sub-problem 
    Like Divide and Conqure, Dynamic Progamming(DP) combines solution to sub-problems.
    DP(Dynamic Progamming) is mainly used when solution of same sub-problem is needed
    again and again.
    For example let's take Fibonacci Number
        In Fibonacci Series => f(n) = f(n-1) + f(n-2)
        for f(5), we will have 
                                          f(5)
                  f(4)                      +             f(3)
          {f(3)     +       f(2)}           +       {f(2)   +   f(1)}
     {f(2) + f(1)}  +   {f(1) + f(0)}       +   {f(1) + f(0)}
 {f(1) + f(0)} 

As we can see some of them are called again and again. Instead of computing
them again and again, we can use the old store value.
We have 2 different methods for storing and reusing the value 
i. Memoization (Top Down)
ii. Tabulation (Bottom Up)


"""

# trying Top Down approch

n = 9  # Fibonacci number = n
arr = [0]*(n+1)  # arr = [0, 0, 0, ......(n times)]
print(n, arr)

def fb(n, arr):  # still can be improved a lot

    if n == 0 or n == 1:  # basic condition
        arr[n] = n
 
    else:  # Fibonacci series
        arr[n] = fb(n-1, arr) + fb(n-2, arr)   

    print(n, arr)  

    
    return arr[n]  # answer

def looks(n, arr):
    return "Fibonacci number is", fb(n, arr)  # just to see in better way

print()
print(looks(n, arr))

 
del n, arr, fb, looks


# TRYING Bottom Up approch

n = 9  # Fibonacci number = n

def fib(n):

    arr = [0]*(n+1)  # arr = [0, 0, 0, ......(n times)]
    arr[1] = 1
    print(arr)

    for i in range(2, n+1):  # calculating the fibonacci and storing the values
        arr[i] = arr[i-1] + arr[i-2]
        print(arr)

    return arr[n]  # answer

def lookss(n):
    return "Fibonacci number is", fib(n)  # just to see in better way

print()
print(lookss(n))
 
del n, lookss, fib

print()
print("Seems like Bottom Up approch is faster and easier")
print()
