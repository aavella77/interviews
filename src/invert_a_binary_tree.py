# To invert a binary tree, you can perform a depth-first search (DFS) on the tree and swap the left and right child nodes at each node. This can be done recursively. Here is the Python code for it:

from collections import deque

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# To print the tree using Depth-First Search (DFS) with recursion, you can use the pre-order, in-order, or post-order traversal methods. Here's an example of how you can modify the print_tree method to use in-order traversal (left, root, right) with recursion:
#
# In this code, the print_tree method first recursively prints the left subtree, then the root node, and finally the right subtree. This is done by calling print_tree on self.left and self.right before and after printing self.val, respectively.

	def print_tree_1(self):
		if self.left:
			self.left.print_tree_1()
		print(self.val, end=",")
		if self.right:
			self.right.print_tree_1()

	# To modify the print_tree method to get the output in the format [4,7,2,9,6,3,1], you can use a breadth-first search (BFS) approach. This approach visits all the nodes at the current level before going to the next level. This is also known as level-order traversal.  Here's how you can modify the print_tree method:

	# In this code, we use a queue to keep track of nodes to visit. We start by adding the root node to the queue. Then, we enter a loop that continues until the queue is empty. In each iteration of the loop, we remove a node from the front of the queue, add its value to the result list, and add its children (if any) to the back of the queue. This process continues until all nodes have been visited, resulting in a level-order traversal of the tree. Finally, we print the result list.
	def print_tree(self):
		queue = deque([self])
		result = []
		while queue:
			node = queue.popleft()
			result.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		print(result)

class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
		return root

# In this code, `invertTree` is a recursive function that inverts a binary tree. It does this by swapping the left and right child nodes of each node in the tree. The base case for the recursion is when the root is `None`, in which case it simply returns `None`.

my_tree = TreeNode(4)
my_tree.left = TreeNode(2)
my_tree.right = TreeNode(7)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(3)
my_tree.right.left = TreeNode(6)
my_tree.right.right = TreeNode(9)

solution = Solution()
inverted_tree = solution.invertTree(my_tree)
print(inverted_tree)

my_tree = TreeNode(2)
my_tree.left = TreeNode(1)
my_tree.right = TreeNode(3)

print("Original Tree:")
my_tree.print_tree()

solution = Solution()
inverted_tree = solution.invertTree(my_tree)

print("\nInverted Tree:")
inverted_tree.print_tree()

print("--------------------")
my_tree = TreeNode(4)
my_tree.left = TreeNode(2)
my_tree.right = TreeNode(7)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(3)
my_tree.right.left = TreeNode(6)
my_tree.right.right = TreeNode(9)

print("Original Tree:")
my_tree.print_tree()

solution = Solution()
inverted_tree = solution.invertTree(my_tree)

print("\nInverted Tree:")
inverted_tree.print_tree()

print("--------------------")
my_tree = TreeNode(4)
my_tree.left = TreeNode(2)
my_tree.right = TreeNode(7)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(3)
my_tree.right.left = TreeNode(6)
my_tree.right.right = TreeNode(9)

print("Original Tree:")
my_tree.print_tree_1()

solution = Solution()
inverted_tree = solution.invertTree(my_tree)

print("\nInverted Tree (inorder transversal):")
inverted_tree.print_tree_1()