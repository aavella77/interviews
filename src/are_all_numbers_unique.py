# WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

# Plan:
# 1. Define a function are_all_numbers_unique() which takes a list as input.
# 2. Convert the list to a set using set() function.
# 3. If the length of the set is equal to the length of the list, return True.
# 4. Otherwise, return False.

def are_all_numbers_unique(list):
	print(list)
	if len(list) == len(set(list)):
		print("all numbers are unique")
	else:
		print("numbers in list are NOT unique")

are_all_numbers_unique([1,2,3])
are_all_numbers_unique([1,2,3,3])