
""" Steps to make Recursion easier
1. what's the simplest case possbile input(Base Case)
    we know the answer of simpler case and share it with computer
    basically making it stop
2. Playing around with examples and visualizing it (trying to understand it)
3. Relating harder case with simpler case
4. Generalizing the pattern
5. Writing code by combining generalizied case with base case

"""
# questions from => https://towardsdatascience.com/10-popular-coding-interview-questions-on-recursion-2ddd8aa86039

# Q1 Sum of n numbers

sum_zero = 0
sum_one = 1 # 1. Base Case

# 2. playing around
s_0 = 0 # Base Case
s_1 = 1 # s_1 = 1 + s_0
s_2 = 3 # s_2 = 2 + s_1
s_3 = 6 # s_3 = 3 + s_2
s_4 = 10
s_5 = 15 # 3. Relating them

n = 9
s_n = n + (n-1) # s_n = n + s_(n-1) ==> 4. Generalizing pattern

def formula_sum(num): # 5. Writing code

    if num == 1 : # with base case and 
        return 1
    
    return formula_sum(num-1) + num # generalized case


sum_num = 5
print("formula_sum :", formula_sum(sum_num)) # Thankfully it worked in one go

# ...............................................................

# Q2 factorial of a number.

factorial_of_a_number0 = 1 # 1. Base case (simplest possible case)
factorial_of_a_number1 = 1 
factorial_of2 = 2 # 2. Playing with them
factorial_of3 = 6 
factorial_of4 = 24 # fac4 = 4*fac3 ==> 3. harder to simpler
factorial_of5 = 120 # 4. generalizing it ==> fac(n) = n*fac(n-1)

def fac_num(num):

    if num in [0, 1]:
        return 1

    return num*fac_num(num-1)

let_num = 5
print("fac_num :", fac_num(let_num))


# ..................................................................

# Q3 Fibonacci number or Fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, .....

Fibonacci_number0 = 0
Fibonacci_number1 = 1 # 1. base case
Fibonacci_of2 = 1 
Fibonacci_of3 = 2 # 2. playing
Fibonacci_of4 = 3 # 3. hard to easy => fib(4) = fib(3) + fib(2)
Fibonacci_of5 = 5 # 4. general => fib(n) = fib(n-1) + fib(n-2)

def fibon_numb(numb):

    if numb in [0, 1]:
        return numb

    return fibon_numb(numb-1) + fibon_numb(numb -2)

Fibonacci_numb = 6
print("Fibonacci_numb :", fibon_numb(Fibonacci_numb))

# ..................................................................

# Q4 product_of_list

input_list = [2, 4, 8, 16] # 2*(2*2)*(2*2*2)*(2*2*2*2) = 2**10 = 1024

def product_of_list(in_list, len_list):

    if len_list == 0:
        return in_list[len_list]

    return in_list[len_list] * product_of_list(in_list, len_list-1)

print('product_of_list :', product_of_list(input_list, len(input_list) - 1))


# ..........................................................................
