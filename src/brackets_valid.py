# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

# Plan:
# 1. Create a dictionary bracket_map to map closing brackets to their corresponding opening brackets.
# 2. Initialize an empty stack to store the opening brackets.
# 3. Iterate through each character in the input string s.
# 4. If the character is a closing bracket, check if the stack is empty
# 5  or the top element of the stack is not the corresponding opening bracket. If either condition is met, return False.
# 5. If the character is an opening bracket, append it to the stack.
# 6. After iterating through all characters, check if the stack is empty. If it is, return True; otherwise, return False.
# 7. The time complexity is O(n), where n is the length of the input string s. The algorithm iterates through each character in the string once.
# 8. The space complexity is O(n) in the worst case, where n is the length of the input string s. This occurs when all characters are opening brackets and are stored in the stack.

def are_symbols_balanced(symbols):
	symbols = symbols.replace(" ", "") # remove spaces from the string
	print(f"symbols: {symbols}")

	# This dictionary maps each closing bracket to its corresponding opening bracket:
	brackets = {
		"}": "{",
		"]": "[",
		")": "("
	}

	stack = []
	# The stack should not be initialized with the first symbol.

	for symbol in symbols:
		print("Analyzing symbol: ", symbol)
		if symbol in brackets: # this will check if symbol is a closing symbol

			print(f"It is a closing symbol: {symbol}")

			if not stack:
				return False   # if the stack is empty return False, (mismatched closing bracket)

			print(f"stack: {stack}")

			top = stack.pop()  # get the OPENING symbol at the top of the stack

			print(f"top: {top} brackets[symbol]: {brackets[symbol]}")

			if top != brackets[symbol]:  # The top of the stack has a opening bracket, the current symbol is is a closing symbol, compare dict of closing symbol has value of opening type of brackets.
				return False
		else: # Otherwise, symbol is an opening symbol, append it to the stack
			print(f"Appending opening symbol to the top of the stack: {symbol}")
			stack.append(symbol)

	return not stack # If the stack is empty, return True, else False. The function should return True only if the stack is empty at the end of the iteration (ensuring all opening brackets have been properly closed).

print(are_symbols_balanced("()"), end="\n\n") # True
print(are_symbols_balanced("{}[]()"), end="\n\n") # True
print(are_symbols_balanced("{}[](}"), end="\n\n") # False
print(are_symbols_balanced(""), end="\n\n") # True
print(are_symbols_balanced("{{{}}}[]()"), end="\n\n") # True
print(are_symbols_balanced(")"), end="\n\n") # False
print(are_symbols_balanced("(]"), end="\n\n") # False
print(are_symbols_balanced("{[()]} ([]{}()) (((())))"), end="\n\n") # True
print(are_symbols_balanced("(([{]) [}([){] "), end="\n\n") # False



