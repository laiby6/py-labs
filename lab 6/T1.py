def dfs(graph, start_node, goal_node):
    stack = [start_node]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(f"Visiting: {current_node}")
            visited.add(current_node)

            if current_node == goal_node:
                print(f"Goal node {goal_node} found!")
                return

            
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("Goal node not found.")
dataGraph = {
    'A': {'B', 'F','D','E'},
    'B': {'K', 'J'},
    'C': {},
    'D': {'G'},
    'E': {'C','H','I'},
    'F': {},
    'G': {},
    'H': {},
    'I': {'L'},
    'J': {},
    'K': {'N','M'},
    'L': {},
    'M': {},
    'N': {}
}


start_node = 'A'
goal_node = 'G'

dfs(graph, start_node, goal_node)