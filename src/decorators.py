# Explanation:
#
# 1. The logging_decorator takes a function func as its argument.
# 2. It defines a nested function wrapper that wraps the original function's logic.
# 3. The wrapper logs information about the function call (name, arguments) before calling the original function func.
# 4. After func executes, the wrapper logs the return value.
# 5. Finally, the wrapper returns the result.
# The add function is decorated with @logging_decorator, applying the logging behavior.
# In summary:
#
# Decorators are a powerful tool in Python for extending functionality and promoting code organization. They provide a clean and flexible way to modify function behavior without altering their core implementation.
def logging_decorator(func):
	"""Decorator that logs function calls."""
	def wrapper(*args, **kwargs):
		print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
		result = func(*args, **kwargs)
		print(f"Function {func.__name__} returned: {result}")
		return result
	return wrapper

my_dict = {"name": "Alejandro", "Age": 52}

@logging_decorator
def add(x, y, **my_dict):
	"""Simple function to add two numbers."""
	return x + y

# Calling the decorated function
result = add(5, 3, **my_dict)
print(result)  # Output: 8

# In Python, decorators are a powerful and versatile design pattern that allows you to modify the behavior of functions or methods without permanently altering their source code. They achieve this by adding functionality "on top" of the original function.
#
# Here's a breakdown of the concept:
#
# Concept:
#
# A decorator is a function that takes another function as its argument and returns a modified version of that function.
# The modified function typically retains the original function's functionality while adding new behavior before, after, or around its execution.
# How it Works:
#
# Define the Decorator: You create a function that encapsulates the additional behavior you want to apply. This function often takes the original function as its argument.
# Apply the Decorator (using the @ symbol): You place the @ symbol followed by the decorator function name before the definition of the function you want to modify.
# Benefits of Decorators:
#
# Code Reusability: You can create reusable decorators that encapsulate common functionality and apply them to multiple functions.
# Maintainability: Modifications are centralized in the decorator, keeping the original function code clean.
# Separation of Concerns: Decorators promote modularity by separating core functionality from aspects like logging, authentication, or performance measurement.
