# Find the longest palindrome substring in a string

def is_palindrome(string):
	reversed_string = "".join(reversed(string))
	return string == reversed_string

def is_palindrome_2(word):
	if word == word[::-1]:
		return True
	else:
		return False

def palindrome_max_sub_string(string_dirty):
	string = [c for c in string_dirty.lower() if c.isalnum()]
	string = "".join(string)
	maximum_palindrome_len = 0
	palindrome_word = ""
	for idx in range(len(string)):
		for idy in range(1, len(string) + 1):
			if is_palindrome(string[idx:idy]):
				if len(string[idx:idy]) > maximum_palindrome_len:
					maximum_palindrome_len = len(string[idx:idy])
					palindrome_word = string[idx:idy]
	return palindrome_word, maximum_palindrome_len

print(palindrome_max_sub_string("aba"))
print(palindrome_max_sub_string("ababbxbb"))
print(palindrome_max_sub_string("ababbxbb123"))
print(palindrome_max_sub_string("A man, a plan, a canal: Panama"))
print(palindrome_max_sub_string("race a car"))
print(palindrome_max_sub_string("race a caraaaa"))
print(palindrome_max_sub_string("ababbaabbccdccbbaaxbb"))