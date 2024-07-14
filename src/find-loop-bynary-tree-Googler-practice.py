# Q) You are given a binary tree of N nodes. While it is mostly a valid binary tree, there is at most one extra edge that violates the binary tree property of having exactly one path from the root to any node. Your job is to design an algorithm to find that extra edge and eliminate it.
#
# Example:
# 0
# / \
# v    v
# 1 <- 2

# DOES NOT SEEM TO WORK
def dfs_cycle_detection_directed(graph, num_nodes):
	def dfs(node):
		visited[node] = True
		recursion_stack[node] = True

		for neighbor in graph[node]:
			if not visited[neighbor]:
				if dfs(neighbor):
					return True
			elif recursion_stack[neighbor]:
				return True

		recursion_stack[node] = False
		return False

	visited = [False] * num_nodes
	recursion_stack = [False] * num_nodes

	for node in range(num_nodes):
		if not visited[node]:
			if dfs(node):
				return True

	return False

  #   0
  #  / \
  # 1 -- 2

graph1 = {
	0: [1, 2],
	1: [0],
	2: [0, 1]
}  # Loop

#    0
#   / \
#   1  2
#  / \ \
# 3  4 - 5


graph2 = {
	0: [1, 2],
	1: [0, 3, 4],
	2: [0, 5],
	3: [1],
	4: [1, 5],
	5: [2, 4]
}  # Loop

graph3 = {
	0: [1,2],
	1: [0],
	2: [0]
}  # No Loop

print(dfs_cycle_detection_directed(graph1, 3))
print(dfs_cycle_detection_directed(graph2, 6))
print(dfs_cycle_detection_directed(graph3, 3))




