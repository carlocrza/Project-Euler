#Prob 3: Largest Prime Factor (of 600851475143)
def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	k = 2
	while(k <= sqrt(n)):
		if n % k == 0:
			return False
		k += 1
	return True

def is_factor(n, factor):
	if n % factor == 0:
		return True
	else:
		return False

def largest_prime_factor(n, start):
	if start % 2 == 0:
		start -= 1
	largest = 0
	while(start < sqrt(n)):
		if(is_factor(n, start) and is_prime(start)):
			largest = start
		start += 2
	return largest
  
  
solution = largest_prime_factor(600851475143)
