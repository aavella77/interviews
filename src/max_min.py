# Given a list of numbers, write a script to find the maximum or minimum value.

def maximum_minimum(nums):
	return max(nums), min(nums)

print(maximum_minimum([1,2,3,4,5]))
print(maximum_minimum([1,0,20,-10,5]))
