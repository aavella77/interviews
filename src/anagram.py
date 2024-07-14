#
# Code
# Testcase
# Testcase
# Test Result
# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return sorted(s) == sorted(t)

# Time complexity: O(nlogn)
# Space complexity: O(n)
# The time complexity is O(n log n). This is because the function uses the sorted function on the input strings s and t. The sorting operation in Python typically uses a variant of Timsort, which has a worst-case and average time complexity of O(n log n), where n is the number of elements being sorted. In this case, n would be the length of the input strings.
# The space complexity is O(n). This is because the sorted function returns a new list containing all the elements from the input string. In the worst case, this list will have the same length as the input string, leading to a space complexity of O(n). Here, n is the length of the input strings.

my_solution = Solution()
print(my_solution.isAnagram("anagram", "nagaram")) # True
print(my_solution.isAnagram("rat", "car")) # False
