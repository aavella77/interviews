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

# Example usage
graph = {
	0: [1],
	1: [2],
	2: [0, 3],
	3: []
}
num_nodes = 4

print(dfs_cycle_detection_directed(graph, num_nodes))  # Output: True
