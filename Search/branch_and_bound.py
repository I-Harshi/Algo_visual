import math

def branch_and_bound(graph, start, goal):
    queue = [(0, start, [start])]
    best_cost = math.inf 
    best_path = None 

    while queue:
        queue.sort(key=lambda x: x[0])
        current_cost, current_node, path = queue.pop(0)
        if current_node == goal:
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = path

        for neighbor, properties in graph.get(current_node, {}).items():
            if neighbor not in path: 
                new_cost = current_cost + properties.get('weight', 1)  # Giving Default weight = 1
                new_path = path + [neighbor]

                if new_cost < best_cost:
                    queue.append((new_cost, neighbor, new_path))

    if best_path:
        return best_path, best_cost
    else:
        return None, math.inf
