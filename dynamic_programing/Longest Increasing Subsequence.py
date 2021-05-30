
# We use DP Bottom-Up approch (To find: lenght of LIS)

l = [10, 22, 9, 33, 21, 50, 41, 160] # given list

def lin(arr): 

	n = len(arr) # lenght of given list(l)
	l_new = [1]*n # new list with same as l
 
	for i in range(1, n): # then we loop to l and l_new
		for j in range(0, i): 
			if arr[i] > arr[j] and l_new[i] < l_new[j] + 1:
				l_new[i] = l_new[j] + 1 # updating it accordinly 

	maxi = 0 # new variable to know the LIS lenght

	for k in range(n):
		maxi = max(maxi, l_new[k]) # updating it accordinly

	return maxi 

print()
print("LIS lenght:", lin(l))

del l, lin


# .........................................................................................

# same problem with greedy methon (recurive calls)

l = [10, 22, 9, 33, 21, 50, 41, 160]

global maxi 
maxi = 1 # global variable to store the maximum

def looks(arr): # function just for looks

	n = len(arr) # lenght of arr

	lis(arr, n) # to main function

	return  maxi # final answer

def lis(arr, n): # main function

	global maxi # access to global variable

	if n == 1: # base case
		return 1

	new_maxi = 1 # lenght of LIS ending with arr[n-1]

	for i in range(1, n): 
		recursive_calls = lis(arr, i) # Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
		if arr[i - 1] < arr[n - 1] and (recursive_calls + 1) > new_maxi:
			new_maxi = recursive_calls + 1 # If arr[n-1] is smaller than arr[n-1], thrn update new_maxi

	maxi = max(maxi, new_maxi) # compare and update

	return new_maxi

print("lenght:", looks(l))

