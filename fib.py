#Python Program to Print Fibonacci Sequence

fibonacci_cache = {}

def fibonacci(n):
	#If we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	#Compute the Nth term
	if n == 0:
		value = 0
	elif n == 1 or n == 2:
		value = 1
	else:
		value = fibonacci(n-1) + fibonacci(n-2)

	#Cache the value and return it
	fibonacci_cache[n] = value
	return value


for n in range (0,100):
	print (n, ":", fibonacci(n))