# Fibonacci Sequence:
# Write a Python function to generate the Fibonacci sequence up to a given number n.
def fibonacci(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return fibonacci(n - 2) + fibonacci(n - 1)
for n in range(10):
	print(fibonacci(n))

# Write fibonacci function without recursion
def fibonacci_without_recursion(n):
	a = 0
	b = 1
	output = []
	for _ in range(n):
		output.append(b) # Update fibonacci sequence
		a, b = b, a + b  # Update a to the previous value of b, b to the current fibonacci a + b
	return output

print(fibonacci_without_recursion(10))

def fibonacci_generator(n):
	"""
	This function generates the Fibonacci sequence up to the nth term using yield.
	Args:
		n: The number of terms in the Fibonacci sequence to generate.
	Yields:
		Each Fibonacci number in sequence.
	"""

	a, b = 0, 1
	for _ in range(n):
		yield b
		a, b = b, a + b

# Example usage:
number_of_terms = 10
for num in fibonacci_generator(number_of_terms):
	print("Using yield: ", num)

def fib(n):
	p, q = 0, 1
	while(p < n):
		yield p
		p, q = q, p + q
x = fib(10)    # create generator object

## iterating using __next__(), for Python2, use next()
x.__next__()    # output => 0
x.__next__()    # output => 1
x.__next__()    # output => 1
x.__next__()    # output => 2
x.__next__()    # output => 3
x.__next__()    # output => 5
x.__next__()    # output => 8


## iterating using loop
for i in fib(10):
	print(i)    # output => 0 1 1 2 3 5 8