# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
	def twoSum(self, nums, target: int):
		output = []
		for idx in range(0, len(nums)-1):
			for idy in range(idx+1, len(nums)):
				if (nums[idx] + nums[idy]) == target:
					output.append(idx)
					output.append(idy)
		return output

# The time complexity of the provided solution is O(n^2), where n is the length of the input list nums. This is because for each element in the list, the solution iterates over the rest of the list to find a pair that sums up to the target. In the worst-case scenario, this results in a quadratic number of operations.
#
# The space complexity of the solution is O(1). This is because the space used does not grow with the size of the input list nums. The output list will always hold at most two elements, regardless of the size of the input.



# This problem can be solved using a hash table (also known as a dictionary in Python). The idea is to iterate through the array and for each element, calculate the complement (target - element). If the complement is not in the hash table, add the current element to the hash table. If the complement is in the hash table, that means we have found two numbers whose sum is equal to the target, so we return their indices.
	def twoSumCopilot(self, nums, target):
		num_dict = {}  # Dictionary to store the number and its index, keeps track if we have seen this number and its location.
		for i, num in enumerate(nums):  # Iterate through the list with index
			complement = target - num  # Calculate the complement
			if complement in num_dict:      # Check if the complement is in the dictionary
				return [num_dict[complement], i]  # If found, return the indices
			num_dict[num] = i  # Add the number and its index to the dictionary
		return []

	def TwoSumRetry(self, nums, target):
		num_dict = {}
		for i, num in enumerate(nums):
			# target = num + complement
			complement = target - num
			if complement in num_dict:
				return [num_dict[complement], i]
			num_dict[num] = i
		return []


# The time complexity of this function is O(n), where n is the length of the input list nums. This is because the function iterates over the list nums once, performing a constant amount of work for each element (calculating the complement and updating the dictionary).
#
# The space complexity of this function is O(n), where n is the length of the input list nums. This is because in the worst-case scenario, every element from nums is stored in the dictionary num_dict. The space used by the dictionary grows linearly with the size of the input.
my_solution = Solution()
print("Two Sum - Brute Force")
print(my_solution.twoSum([2,7,11,15], 9)) # [0, 1]
print(my_solution.twoSum([3,2,4], 6)) # [1, 2]
print(my_solution.twoSum([3,3], 6)) # [0, 1]

print("Two Sum - Copilot")
print(my_solution.twoSumCopilot([2,7,11,15], 9)) # [0, 1]
print(my_solution.twoSumCopilot([3,2,4], 6)) # [1, 2]
print(my_solution.twoSumCopilot([3,3], 6)) # [0, 1]

print("Two Sum - Retry")
print(my_solution.TwoSumRetry([2,7,11,15], 9)) # [0, 1]
print(my_solution.TwoSumRetry([3,2,4], 6)) # [1, 2]
print(my_solution.TwoSumRetry([3,3], 6)) # [0, 1]

