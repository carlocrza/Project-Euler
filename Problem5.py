# Problem 5: What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

def divisible():
	nums = [i for i in range(1,21)]
	print(nums)
	start = 200000000  #start at a very large number because this method is brute-force
	while True:
		test = 0
		for i in nums:
			print(start)
			if not (start % i == 0):
				test += 1
		if test == 0:
			return start
		start += 20
