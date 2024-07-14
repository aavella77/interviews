# Given a sorted array of integers, return the index of the given key. Return -1 if the key is not found.
# Implement binary search recursively.

def binary_search_recursive(arr, target, left, right):
	if left > right:
		return -1

	mid = (left + right) // 2

	print(f"Searching in {arr[left:right+1]}, mid: {mid}")

	if arr[mid] == target:
		print(f"the target is located at {mid}")
	elif arr[mid] < target:
		return binary_search_recursive(arr, target, mid + 1, right)
	else:
		return binary_search_recursive(arr, target, left, mid - 1)

binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 0, 9)  # 4
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0, 9)  # 0
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 0, 9)  # 9
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 0, 9)   # 6
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 0, 9)   # -1
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0, 9)  # -1
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 0, 9)   # 5
binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 0, 9)   # 7

