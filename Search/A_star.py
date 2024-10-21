import heapq

def a_star_search(graph, start, goal, heuristic):

    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f_cost, g_cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)


        if current == goal:
            return path, g_cost


        for neighbor in graph[current]:
            if neighbor not in visited:
                edge_cost = graph[current][neighbor]['weight']
                new_g_cost = g_cost + edge_cost
                new_f_cost = new_g_cost + heuristic[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_f_cost, new_g_cost, neighbor, new_path))

    return None, float('inf')  # If no path is found
