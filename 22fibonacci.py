def fibonacci(n):
	fib_sequence = (0, 1)
	for i in range(2, n):
		fib_sequence = fib_sequence + (fib_sequence[-2] + fib_sequence[-1],)
	return fib_sequence
print(fibonacci(10))