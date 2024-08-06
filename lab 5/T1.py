from collections import deque  #import library


def bfs(graph, start_node, goal_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        print(f"Visiting: {current_node}")

        if current_node == goal_node:
            print(f"Goal node {goal_node} found!")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("Goal node not found.")

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'

bfs(graph, start_node, goal_node)

