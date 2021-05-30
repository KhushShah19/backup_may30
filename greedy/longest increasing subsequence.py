array = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(array)

final_maximum = 0

max_list = 0


def gfg_lis(l, arr):
    global final_maximum
    global max_list

    if l == 1:
        return 1

    for i in range(1, l):
        sample_value = gfg_lis(i, arr)
        # print("s_v :", sample_value)
        if arr[i - 1] > arr[l - 1] and sample_value > max_list:
            max_list = sample_value + 1
            # print("max_list ..................... :", max_list)

    final_maximum = max(max_list, final_maximum)
    # print("f_max :", final_maximum)

    return max_list


print(gfg_lis(n, array))
print()
print("final_maximum :", final_maximum)

# ......................................................................................................

list_given = [2, 4, 3, 6, 5, 9, 7, 8]
len_lis = len(list_given)
longest_len = 1


def to_find(arr_given, len_arr):
    
    global longest_len

    
     




# ....................................................................................................
# A naive Python implementation of LIS problem
""" To make use of recursive calls, this function must return
two things:
1) Length of LIS ending with element arr[n-1]. We use
max_ending_here for this purpose
2) Overall maximum as the LIS may end with an element
before arr[n-1] max_ref is used this purpose.
The value of LIS of full array of size n is stored in
*max_ref which is our final result """

# global variable to store the maximum
global maximum


def _lis(arr, n):
    # to allow the access of global variable
    global maximum
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
	IF arr[n-1] is maller than arr[n-1], and max ending with
	arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    # to allow the access of global variable
    global maximum

    # lenght of arr

    n = len(arr)

    # maximum variable holds the result

    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, n)

    return maximum


# Driver program to test the above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print(lis(arr))
# print("Length of lis is ", lis(arr)

print("........")

print()














