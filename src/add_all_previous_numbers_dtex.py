# nums = [1,2,3,4,5] -> output = [1,3,6,10,15]
# Add the numbers in the list to the previous numbers in the list

# Optimized solution using slicing
# Plan:
# 1. Initialize output first entry to the first entry in the array
# 2. Iterate from 1 to len(arr)
# 3. Append to the output (current + all previous numbers)
def sum_previous_numbers(arr):
	output = []
	output.append(arr[0])
	for idx in range(1, len(arr)):
		output.append(arr[idx] + sum(arr[0:idx]))
	return output

print(sum_previous_numbers([1, 2, 3, 4, 5]))
print(sum_previous_numbers([2, 2, 2, 2, 2]))



# Approach 1:
# 2 for loops:
# Append the first number to output
# for loop iterates over numbers starting at one,
# the second to sum previous numbers (note: is to idx).
# current_sum starts numbers[idx]
# This problem appeared on DTEX interview

def add_all_previous_numbers(numbers):
	output = []
	output.append(numbers[0])
	for idx in range(1, len(numbers)):
		current_sum = numbers[idx]
		for idy in range(idx):
			current_sum = current_sum + numbers[idy]
		output.append(current_sum)
	return output

print(add_all_previous_numbers([1,2,3,4,5])) # [1,3,6,10,15]
print(add_all_previous_numbers([-1,2,3,-4,5])) # -1, 1, 4, 0, 5
print(add_all_previous_numbers([1,2,3,4,5,6])) # [1,3,6,10,15,21]
print(add_all_previous_numbers([1,2,3,4,5,6,7])) # [1,3,6,10,15,21,28]


# Note: The range function in Python generates a sequence of numbers starting from
# 0 and ending at idx - 1. If idx is 0, range(0) produces an empty sequence.
# Therefore, the loop body will not execute at all.

# When idx is 1, the for loop for idy in range(idx): runs 1 time. Here's why:
# The range function in Python generates a sequence of numbers starting from 0 and ending
# at idx - 1. If idx is 1, range(1) produces a sequence containing a single number,
# [0]. Therefore, the loop body will execute once.
