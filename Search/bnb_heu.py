import heapq

def branch_and_bound_heuristics(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        total_cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, total_cost

        for neighbor in graph[current]:
            if neighbor not in visited:
                cost = graph[current][neighbor]['weight']
                new_cost = total_cost - heuristic[current] + cost + heuristic[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, neighbor, new_path))

    return None, float('inf')
