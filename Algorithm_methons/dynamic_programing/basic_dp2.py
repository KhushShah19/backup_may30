
# Dynamic Programing are of two types
# 1. Tabulation Method – Bottom Up and 2. Memoization Method – Top-Down

# 2. Memoization Method – Top-Down (recursion + memorization)


def fibonacci(n):

    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))





fibon_list = []

def fibon(n):

    if len(fibon_list) == n:
        print(len(fibon_list))

    elif n in 0 or 1:
        fibon_list.append(n)

print(fibon(6))


