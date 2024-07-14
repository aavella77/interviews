# Broadcom - interview: Given a List (List of words as it will be in a dictionary) and a string, write a function to determine if the string can be formed by breaking it into words from the dictionary (allowing spaces between words).

# Input1: dictionary = ["apple", "pear", "pie"] ; string = "applepie"       --> Returns: True
# Input2: dictionary = ["apple", "pear", "pie"] ; string = "pappleie"       --> Returns: False
# Input3: dictionary = ["apple", "pear", "pie"] ; string = "applepiegreen"  --> Returns: False
# Input4: dictionary = ["apple", "pear", "pie"] ; string = "apple pie"      --> Returns: True
# Input5: dictionary = ["ate","cat","eagle"] ; string = "cateagle"          --> Returns: True
# Input6: dictionary = ["ate","cat","eagle"] ; string = "cateag"            --> Returns: False


# Output: True/False

def word_break(dictionary, string):
	# your solution ->
	print("-----------------")
	print(f"dictionary = {dictionary}")
	print(f"string = {string}")
	# Remove spaces from the string
	string = string.replace(" ", "")

	# Create a list of booleans to store the results of subproblems (substrings of the input string)
	dp = []  # dp[i] will be True if dp[0:i] can be segmented into words from the dictionary

	# Initialize dp with False values for all indices from 0 to len(string) + 1 (inclusive)
	# dp means dynamic programming
	for _ in range(len(string) + 1):
		dp.append(False)

	dp[0] = True  # Base case

	# Iterate over the input string
	for i in range(1, len(string) + 1):
		# Iterate over the input string from 0 to i
		for j in range(i):
			# Check if dp[j] is True and the substring from j to i is in the dictionary
			if dp[j] and string[j:i] in dictionary:
				print(f"dp[j] = {dp[j]} string[j:i] = {string[j:i]}")
				# If dp[j] is True (i.e., dp[0:j] can be segmented into words from the dictionary)
				# and the substring from j to i is in the dictionary, then dp[i] is True
				dp[i] = True
				break
	return dp[len(string)]  # Return the value of dp[len(string)]
							# which indicates whether the entire input string can be segmented into words from the dictionary

dictionary = ["apple", "pear", "pie"]
string = "applepie"
print(word_break(dictionary, string)) # True

dictionary = ["apple", "pear", "pie"]
string = "pappleie"
print(word_break(dictionary, string)) # False

dictionary = ["apple", "pear", "pie"]
string = "applepiegreen"
print(word_break(dictionary, string)) # False

dictionary = ["apple", "pear", "pie"]
string = "apple pie"
print(word_break(dictionary, string)) # True

dictionary = ["ate","cat","eagle"]
string = "cateagle"
print(word_break(dictionary, string)) # True

dictionary = ["ate","cat","eagle"]
string = "cateag"
print(word_break(dictionary, string)) # False

