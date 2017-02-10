#PROBLEM 6
def diff_square(x=100):
  """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
	#1 + 2 + 3 + 4 ... + n === (n/2) * (n+1)
	#(n/2) sets of n+1
	#1 + 2 + 3 + 4 ==
	#1 + 2 +
	#4 + 3  --> (4/2) = 2 sets that add up to (4+1) = 5
  
	square_of_the_sum = ((x/2) * (x + 1)) ** 2

	sum_of_the_squares = 0
	while x > 0:
		sum_of_the_squares += x ** 2
		x -= 1

	return square_of_the_sum - sum_of_the_squares
