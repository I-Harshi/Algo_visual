def beam_search(graph, start, goal, beam_width=2):
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        new_queue = []
        
        for (node, path) in queue:
            if node == goal:
                print(f"Path found: {path}")
                return path 
            neighbors = sorted(graph[node].items(), key=lambda x: x[1].get('weight', float('inf')))
            
            for neighbor, _ in neighbors[:beam_width]: 
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_queue.append((neighbor, new_path))
                    visited.add(neighbor) 
        queue = sorted(new_queue, key=lambda x: len(x[1]))[:beam_width]

    print("No valid path found.")
    return None
