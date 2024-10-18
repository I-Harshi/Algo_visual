def hill_climbing_search(graph, start, goal):
    current_node = start
    visited = set([current_node])
    path = [current_node]

    while current_node != goal:
        neighbors = list(graph.neighbors(current_node))
        neighbors = sorted(neighbors, key=lambda x: graph[current_node][x].get('weight', float('inf')))

        next_node = None
        for neighbor in neighbors:
            if neighbor not in visited:  
                next_node = neighbor
                break

        if next_node is None or next_node == current_node:
            break

        current_node = next_node
        visited.add(current_node)
        path.append(current_node)

    if current_node == goal:
        return path
    else:
        return None
