# takes string identify most repeated characters and return word
# Input : Hello World !!
# Output : Hello
#
# Input : Hello World, this is Pineapple !!
# Output : Pineapple
#
# Input : No words !!
# Output : !!
#
# Input : No words.
# Output : -1
from collections import Counter


def word_with_most_repeated_char(string):
	string = string.lower()
	words = string.split(" ")
	max_rep = float("-inf")
	max_word = -1
	for word in words:
		repetitions = Counter(word)
		# print (repetitions)
		for repetition in repetitions.values():
			if repetition > max_rep and repetition > 1:
				max_rep = max(max_rep, repetition)
				max_word = word
	return max_word

print(word_with_most_repeated_char("Hello World !!"))  # Hello
print(word_with_most_repeated_char("Hello World, this is Pineapple !!"))  # Pineapple
print(word_with_most_repeated_char("No words !!"))  # !!
print(word_with_most_repeated_char("No words."))  # -1
print(word_with_most_repeated_char("Hello World, this is Pineapple ppPineapple!!"))  # ppPineapple!!
print(word_with_most_repeated_char("ppPineapple Hello World, this is Pineapple ppPineapple!!"))  # ppPineapple
print(word_with_most_repeated_char("Interview test case Tapan and Alejandro"))  # tapan
print(word_with_most_repeated_char("Alejandro"))  # alejandro
print(word_with_most_repeated_char("Hello World !! Hello World !!"))  # Hello
print(word_with_most_repeated_char("Hello World !! Hello World !!!"))  # !!!
print(word_with_most_repeated_char(""))  # -1
print(word_with_most_repeated_char("aaaaaaaaa bbbb cc dddddddddd eee"))  # dddddddddd
print(word_with_most_repeated_char("aaaa bbbb"))  # aaaa