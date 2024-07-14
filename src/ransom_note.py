# 383. Ransom Note
# Solved
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

# Plan:
# 1. Create a Counter object for the magazine string.
# 2. Iterate through the ransomNote string and check if each character is present in the Counter object.
# 3. If the character is present, decrement its count in the Counter object.
# 4. If the character is not present or its count becomes negative, return False.
# 5. If all characters are successfully matched, return True.

from collections import Counter

def can_construct(ransomNote, magazine):
	print(f"ransomnote: {ransomNote}, magazine: {magazine}")
	char_count = Counter(magazine)  # Create a Counter object for the magazine string

	for char in ransomNote:  # Iterate through the characters in the ransomNote
		if char_count[char] > 0:  # Check if the character is present in the magazine
			char_count[char] -= 1  # Decrement the count of the character
		else:
			return False  # If the character is not present or its count is zero, return False

	return True  # If all characters are successfully matched, return True

# Test cases
print(can_construct("a", "b"))  # False
print(can_construct("aa", "ab"))  # False
print(can_construct("aa", "aab"))  # True
print(can_construct("aa", "a"))  # False
print(can_construct("aa", "aa"))  # True
print(can_construct("abc", "abc"))  # True
print(can_construct("abc", "abcd"))  # False
print(can_construct("abc", "ab"))  # False
print(can_construct("abc", "ac"))  # False
print(can_construct("abc", "bc"))  # False
print(can_construct("abc", "c"))  # False
print(can_construct("abc", "b"))  # False
print(can_construct("abc", "a"))  # False
print(can_construct("abc", "cab"))  # True
print(can_construct("abc", "bac"))  # True
print(can_construct("abc", "bca"))  # True