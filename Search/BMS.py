

def bms_search(graph, start, goal):
    def explore_path(current_path, visited):
        node = current_path[-1]
        if node == goal:
            return current_path  

        lex_paths = [] 

        for neighbor in sorted(graph[node]): 
            if neighbor not in visited:
                new_path = current_path + [neighbor]
                result = explore_path(new_path, visited | {neighbor})
                if result:  
                    lex_paths.append(result)

        return min(lex_paths, key=lambda x: tuple(x)) if lex_paths else None

    visited = {start}
    return explore_path([start], visited)
