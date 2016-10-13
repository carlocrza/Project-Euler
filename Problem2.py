#Problem 2: Even fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

def sum_even_fib(n):
	"""sum even fibonacci numbers up until n"""
	i = 3
	sum = 0
	fib = 0
	while(fib <= n):
		fib = fibonacci(i)
		if(fib % 2 == 0):
			sum += fib
		i += 1

	return sum
