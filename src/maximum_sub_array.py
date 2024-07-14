# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the
# subarray
# with the largest sum, and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
	def maxSubArray(self, nums) -> int:
		print("=====================================")
		print(f"nums: {nums}")
		output = float('-inf')
		for idx in range(len(nums)):
			for idy in range(idx + 1, len(nums) + 1):
				current_sum = sum(nums[idx:idy])
				output = max(current_sum, output)
				print(f"idx={idx} idy={idy} nums[idx:idy] {nums[idx:idy]} sum {sum(nums[idx:idy])} output: {output}")
		return output

# Complexity Analysis
# The time complexity for this approach is O(n^2),
# where n is the length of the input array nums.
# This is because we are iterating over all possible subarrays
# of the input array and calculating their sums.

# The space complexity is O(1) since we are using a
# constant amount of extra space.

# Test cases
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(solution.maxSubArray([1]))  # 1
print(solution.maxSubArray([5,4,-1,7,8]))  # 23
print(solution.maxSubArray([-1]))  # -1
print(solution.maxSubArray([-2,1]))  # 1
print(solution.maxSubArray([-2,-1]))  # -1
print(solution.maxSubArray([1,2]))  # 3
print(solution.maxSubArray([1,2,3]))  # 6
print(solution.maxSubArray([1,2,3,4]))  # 10
print(solution.maxSubArray([1,2,3,4,5]))  # 15
print(solution.maxSubArray([-1,-2,-3,-4,-5]))  # -1


# Kadane's algorithm works by keeping track of the current subarray sum and the maximum subarray sum seen so far. It iterates through the array, and for each element, it calculates the current subarray sum. If the current subarray sum becomes less than the current element, the current subarray sum is set to the value of the current element. The maximum subarray sum is updated whenever the current subarray sum is greater than the maximum subarray sum.

def maxSubArrayKadaneChatGpt(nums):
	current_subarray = max_subarray = nums[0]  # Initialize the variables to the first element of the array


	for num in nums[1:]:  # Start from the second element
		current_subarray = max(num, current_subarray + num)  # Calculate the maximum sum of the subarray ending at the current element
		max_subarray = max(max_subarray, current_subarray)  # Update the maximum sum of the subarray seen so far

	return max_subarray  # Return the maximum sum of the subarray



def maxSubArrayKadaneYouTube(nums):
	max_global = current_sum = nums[0]  # Initialize the variables to the first element of the array

	for num in nums[1:]:  # Start from the second element
		current_sum = max(num, current_sum + num)  # Calculate the maximum sum of the subarray ending at the current element
		if current_sum > max_global:
			max_global = current_sum

	return max_global  # Return the maximum sum of the subarray

# Complexity Analysis
# The time complexity of Kadane's algorithm is O(n), where n is the length of the input array nums.
# This is because the algorithm iterates through the array once to calculate the maximum subarray sum.
# The space complexity is O(1) since the algorithm uses a constant amount of extra space.

# Test cases
print(maxSubArrayKadaneChatGpt([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArrayKadaneChatGpt([1]))  # 1
print(maxSubArrayKadaneChatGpt([5,4,-1,7,8]))  # 23