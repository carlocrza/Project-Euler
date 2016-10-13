#Problem 1: Sum the numbers below 'n' that are
#divisible by 3 or 5. 'n' in this problem's case is 1000
def sum(n):
	return sum_help(n-1)
	
def sum_help(n):
	if(n < 3):
		return 0
	if(n%3 == 0 or n%5 == 0):
		return n + sum_help(n-1)
	return 0 + sum_help(n-1)

sum_numbers = sum(1000)

#The above solution can be converted into a list comprehension
sum_numbers = sum(x for x in range(1000) if 0 in [x %3, x % 5])
