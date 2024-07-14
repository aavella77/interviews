# Broadcom - interview: Given a List (List of words as it will be in a dictionary) and a string, write a function to determine if the string can be formed by breaking (segmented) it into words from the dictionary (allowing spaces between words).

# Input1: dictionary = ["apple", "pear", "pie"] ; string = "applepie"       --> Returns: True
# Input2: dictionary = ["apple", "pear", "pie"] ; string = "pappleie"       --> Returns: False
# Input3: dictionary = ["apple", "pear", "pie"] ; string = "applepiegreen"  --> Returns: False
# Input4: dictionary = ["apple", "pear", "pie"] ; string = "apple pie"      --> Returns: True
# Input5: dictionary = ["ate","cat","eagle"] ; string = "cateagle"          --> Returns: True
# Input6: dictionary = ["ate","cat","eagle"] ; string = "cateag"            --> Returns: False

# Words in the dictionary are sorted.

# Define a recursive function can_form(start) that checks if the substring string[start:] can be formed using words from the dictionary.
def dictionary_can_form_string_recursive(dictionary, string):
	dictionary_set = set(dictionary)  # Convert the list to a set for O(1) lookups
	string = string.replace(" ", "")  # Remove spaces if present
	memo = {}  # Use memoization

	def can_form(start):
		print(f"Checking substring: {string[start:]} starting at index {start}")
		if start == len(string):  # Base case: Return True when we have successfully segmented the entire string
			print("Base case: start == len(string)")
			return True

		if start in memo:  # If we have already seen this problem, return the stored result to avoid recomputation
			print(f"Using memo[{start}] {memo[start]}")
			return memo[start]

		for end in range(start + 1, len(string) + 1):
			print(f"Found {string[start:end]} in dictionary. Checking substring from {end} onwards.")
			if string[start:end] in dictionary_set and can_form(end):
				memo[start] = True
				print(f"Condition met {string[start:end]}")
				print(f"memo[{start}] set to True {memo}")
				return True

		memo[start] = False
		print(f"memo[{start}] set to False {memo}")
		return False

	return can_form(0)

# Test examples
print("Result:", dictionary_can_form_string_recursive(dictionary=["apple", "pear", "pie"], string="applepie"), end="\n\n")  # True
print("Result:", dictionary_can_form_string_recursive(dictionary=["apple", "pear", "pie"], string="pappleie"), end="\n\n")  # False
print("Result:", dictionary_can_form_string_recursive(dictionary=["apple", "pear", "pie"], string="applepiegreen"), end="\n\n")  # False
print("Result:", dictionary_can_form_string_recursive(dictionary=["apple", "pear", "pie"], string="apple pie"), end="\n\n")  # True
print("Result:", dictionary_can_form_string_recursive(dictionary=["ate", "cat", "eagle"], string="cateagle"), end="\n\n")  # True
print("Result:", dictionary_can_form_string_recursive(dictionary=["ate", "cat", "eagle"], string="cateag"), end="\n\n")  # False
print("Result:", dictionary_can_form_string_recursive(dictionary=["ab", "abc", "cd", "def", "abcd"], string="abcdabc"), end="\n\n")  # True
# Complex example to demonstrate memoization
print("Result:", dictionary_can_form_string_recursive(dictionary=["a", "aa", "aaa", "aaaa"], string="aaaaaaa"), end="\n\n")  # True
# Example where memoization is needed
print("Result:", dictionary_can_form_string_recursive(dictionary=["cat", "cats", "and", "sand", "dog"], string="catsandog"), end="\n\n")  # False












