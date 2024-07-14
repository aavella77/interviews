# Approach: using list comprehension find zero and non-zero elements
# and concatenate them.

def move_zeroes_to_the_end(nums):
	output = []
	zeroes = [num for num in nums if num == 0]
	non_zeroes = [num for num in nums if num != 0]
	output = non_zeroes + zeroes
	return output

print(move_zeroes_to_the_end([0,1,0,2,3,0,0,4,0]))
print(move_zeroes_to_the_end([0,1]))
print(move_zeroes_to_the_end([0]))
print(move_zeroes_to_the_end([1]))
print(move_zeroes_to_the_end([1,2,3]))
print(move_zeroes_to_the_end([0,1,2,0]))
print(move_zeroes_to_the_end([0,1,2,0,0,0]))
print(move_zeroes_to_the_end([0,0,0,0]))

def move_zeroes_to_end_string(string):
	zeroes = [c for c in string if c == "0"]
	non_zeroes = [c for c in string if c != "0"]
	return "".join(non_zeroes + zeroes)


print(move_zeroes_to_end_string("0Ale012300"))
print(move_zeroes_to_end_string("0Ale000123"))
print(move_zeroes_to_end_string("Ale1230000"))
print(move_zeroes_to_end_string("0000Ale123"))

def move_zeroes_1(input_string):
	output_string = []
	num_zeroes = 0
	for char in input_string:
		if char != "0":
			output_string.append(char)
		else:
			num_zeroes += 1
	for _ in range(num_zeroes):
		output_string.append("0")

	return "".join(output_string)

# Second solution
print(f"input_string: 0abc0edf0")
print(move_zeroes_1("0abc0edf0"))

print(f"input_string: 000ab0c0e0df000")
print(move_zeroes_1("000ab0c0e0df000"))