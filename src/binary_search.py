#
# Code
# Testcase
# Test Result
# Test Result
# 704. Binary Search
# Easy
# Topics
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution:
	def search(self, nums, target: int) -> int:
		max = len(nums) - 1
		min = 0
		while min <= max:
			mid = (max + min) // 2
			print(f"min {min} max {max} mid {mid}")
			if nums[mid] == target:
				return mid
			elif target > nums[mid]:
				min = mid + 1
			else:
				max = mid - 1
		return -1

# Complexity Analysis
# Time complexity: O(log n)
# Space complexity: O(1)
# The time complexity is O(log n). This is because in each iteration of the while loop, the search space is halved. This is the key characteristic of binary search. Here, n is the size of the input list nums. The logarithmic time complexity results from the fact that with each comparison, the algorithm eliminates half of the possible solutions.
# The space complexity is O(1). This is because the algorithm only uses a constant amount of extra space. The space used does not change with the size of the input list nums. The variables min, max, and mid are used for the computation and they do not depend on the size of the input list. Hence, the space complexity is constant

my_solution = Solution()
print(my_solution.search([-1,0,3,5,9,12], 9))  # 4
print(my_solution.search([-1,0,3,5,9,12], 2))  # -1
print(my_solution.search([5], 5))  # 0
print(my_solution.search([5], 6))  # -1
print(my_solution.search([5], 4))  # -1
print(my_solution.search([-1,0,3,5,9,12], 13))  # -1




