def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # Process vertex
            print(vertex)
            # Push adjacent vertices onto stack
            stack.extend(graph[vertex] - visited)  # subtracting visited nodes
    
    return visited

# Example usage:
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("DFS traversal:")
dfs(graph, 'A')

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            # Process vertex
            print(vertex)
            # Enqueue adjacent vertices
            queue.extend(graph[vertex] - visited)  # subtracting visited nodes
    
    return visited

# Example usage (same graph as before):
print("\nBFS traversal:")
bfs(graph, 'A')
