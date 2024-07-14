# 21. Merge Two Sorted Lists
# Easy
# Topics
# Companies
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Plan:
# 1. Initialize two pointers, current_node_1 and current_node_2, to the heads of the input lists.
# 2. Initialize a dummy node, head, to store the merged list.
# 3. Initialize a pointer, current_output, to the dummy node.
# 4. Iterate over the two lists while both current_node_1 and current_node_2 are not None.
# 5. Compare the values of the current nodes of the two lists.
# 6. Append the smaller value to the merged list and move the corresponding pointer to the next node.
# 7. After the loop, append the remaining list to the merged list.
# 8. Return the next node of the dummy node, which is the head of the merged list.
#
# The time complexity is O(n + m), where n and m are the lengths of the input lists list1 and list2, respectively. The algorithm iterates over both lists once.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
		current_node_1 = list1
		current_node_2 = list2
		head = ListNode(0)
		current_output = head
		while current_node_1 is not None and current_node_2 is not None:
			if current_node_1.val < current_node_2.val:
				current_output.next = ListNode(current_node_1.val)
				current_node_1 = current_node_1.next
			else:
				current_output.next = ListNode(current_node_2.val)
				current_node_2 = current_node_2.next
			current_output = current_output.next

		# Append the remaining list
		current_output.next = current_node_1 if current_node_1 is not None else current_node_2

		return head.next

	def print_list(self, head: ListNode) -> [int]:
		current_node = head
		output = []
		while current_node is not None:
			output.append(current_node.val)
			current_node = current_node.next
		return output

my_solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
head = my_solution.mergeTwoLists(list1, list2)
print(my_solution.print_list(head)) # [1,1,2,3,4,4]

# list1 smaller than list2
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3))
head = my_solution.mergeTwoLists(list1, list2)
print(my_solution.print_list(head)) # [1,1,2,3,4]

# list1 has 5 elements, list2 has 3 elements
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list2 = ListNode(1, ListNode(3, ListNode(4)))
head = my_solution.mergeTwoLists(list1, list2)
print(my_solution.print_list(head)) # [1,1,2,3,3,4,4,5]