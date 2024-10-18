import heapq
import random

def oracle_function(graph, node, goal):
    return min(
        graph[node], 
        key=lambda neighbor: graph[node][neighbor]['weight'] + random.uniform(0, 1)
    )

def oracle_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        total_cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, total_cost

        try:
            next_node = oracle_function(graph, current, goal)
            new_path = path + [next_node]
            new_cost = total_cost + graph[current][next_node]['weight']
            heapq.heappush(pq, (new_cost + heuristic[next_node], next_node, new_path))
        except ValueError:
            return None, float('inf')

    return None, float('inf')
