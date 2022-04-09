
# Top Down vs Bottom Up


# Explain using Fibonacci number or Fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ..... BASE CASE: 0, 1, 1

# 1. Bottom Up approch (Tabulation Method – Dynamic Programming)

def bottom_up(num_tofind):

    
    series_list = [0]*(num_tofind+1) 
    series_list[0], series_list[1] = 0, 1

    for i in range(2, num_tofind+1):

        series_list[i] = series_list[i-1] + series_list[i-2]

    return  series_list


print("series list :", bottom_up(10))



# 2. Top Down approch

ser_list = []

def top_down(to_find):

    if to_find in [0, 1]:
        return to_find

    return top_down(to_find-1) + top_down(to_find-2)

print("series list :", top_down(10))

