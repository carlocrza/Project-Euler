#Prob 4: Find the largest palindrome made from the product of two 3-digit numbers.

def largest(m=3, x=999):  #largest of two 3-digit numbers
	y = x

	i, product, largest_palindrome = 0, 1, 1
	while i <= x - pow(10, m-1):
		while y >= pow(10, m-1):
			product = x * y
			if(is_palindrome(product)):
				if(product > largest_palindrome):
					largest_palindrome = product
			y -= 1
		y = x-1
		i += 1
		x -= 1

	if(y == pow(10, m-1)):
		return "no palindrome apparently"

	return largest_palindrome
	

def is_palindrome(n):
    x, y = n, 0
    f = lambda: y*10 + x % 10

    while x > 0:
        x, y = x // 10, f()
    return y == n
    
    
solution = largest()
