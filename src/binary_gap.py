# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..2,147,483,647].

def solution(N):
	# Implement your solution here
	number_binary = bin(N)
	# print(f"Number in binary {number_binary}")
	number_binary = number_binary.split("0b")[1]
	# print(f"Number in after split binary {number_binary}")
	current_output = 0
	output = 0
	for bit in number_binary:
		# print(f"bit {bit}")
		if bit == "0":
			current_output += 1
			# print(f"current_output {current_output}")
		if bit == "1" and current_output != 0:
			if current_output > output:
				output = current_output
			current_output = 0
	print(f"N: {N} - {number_binary} - output: {output}")
	return output

def solution_github_copilot(N):
	# Convert the number to binary and remove the '0b' prefix
	binary = bin(N)[2:]

	# Initialize variables to keep track of the current gap length and the longest gap length
	current_gap_length = 0
	longest_gap_length = 0

	# Iterate over the binary representation
	for bit in binary:
		if bit == '0':
			# If the bit is 0, increment the current gap length
			current_gap_length += 1
		else:
			# If the bit is 1, update the longest gap length if the current gap length is greater
			longest_gap_length = max(longest_gap_length, current_gap_length)
			# Reset the current gap length
			current_gap_length = 0
	print(f"N: {N} - {binary} - output: {longest_gap_length}")
	return longest_gap_length

solution(1041)
solution(529)
solution(20)
solution(15)
solution(32)
solution(0)
solution(2048)
solution(31)
solution(5)
solution(9)
solution(2147483647)
solution(74901729)

print("Github Copilot solution")
print("-----------------------")

solution_github_copilot(1041)
solution_github_copilot(529)
solution_github_copilot(20)
solution_github_copilot(15)
solution_github_copilot(32)
solution_github_copilot(0)
solution_github_copilot(2048)
solution_github_copilot(31)
solution_github_copilot(5)
solution_github_copilot(9)
solution_github_copilot(2147483647)
solution_github_copilot(74901729)