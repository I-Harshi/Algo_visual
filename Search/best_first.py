import heapq

def best_first_search(graph, start, goal, heuristic):

    pq = [(heuristic[start], start, [start])] 
    visited = set()

    while pq:
        h_value, current_node, path = heapq.heappop(pq)
        if current_node == goal:
            cost = sum(graph[u][v]['weight'] for u, v in zip(path, path[1:]))
            return path, cost

        if current_node not in visited:
            visited.add(current_node)


            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, new_path))

    return None, float('inf')  
