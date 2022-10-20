# Python3 program to implement
# the above approach

# Function to check if it the
# array can be rearranged such
# such that every even indices
# contains an even element
def checkPossible(a, n):
	
	# Stores the count of even elements
	even_no_count = 0

	# Traverse array to count even numbers
	for i in range(n):
		if (a[i] % 2 == 0):
			even_no_count += 1
	
	# If even_no_count exceeds
	# count of even indices
	if (n // 2 > even_no_count):
		print("No")
		return
	
	print("Yes")
	j = 0
	
	for i in range(1, n, 2):
		if (a[i] % 2 == 0):
			continue
			
		else:
			while (j < n and a[j] % 2 != 0):
				j += 2

			a[i] += a[j]
			a[j] = a[i] - a[j]
			a[i] -= a[j]
		
	for i in range(n):
		print(a[i], end = " ")
	
# Driver Code
arr = [ 2, 3, 4, 5, 6, 7 ]
n = len(arr)

checkPossible(arr, n)


