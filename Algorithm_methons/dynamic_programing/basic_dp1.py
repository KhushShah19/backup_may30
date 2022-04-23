
# Dynamic Programing are of two types
# 1. Tabulation Method – Bottom Up and 2. Memoization Method – Top-Down

# 1. Tabulation Method – Bottom Up

def bottom_up(n):

    bup_list = [0, 1]

    for i in range(2, n):
        bup_list.append(bup_list[i-1] + bup_list[i-2])

    return bup_list

print(bottom_up(11))




