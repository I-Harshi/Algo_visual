import networkx as nx
from Create_graphs import create_graph, display_graph

def bms_search(graph, start, goal):
    """
    Perform British Museum Search without using built-in functions.
    Explore all paths in lexicographical order.
    """
    def explore_path(current_path, visited):
        """
        Recursive function to explore all paths from the current node.
        """
        node = current_path[-1]
        if node == goal:
            return current_path  # Goal found, return the path

        lex_paths = []  # Store all valid paths lexicographically

        for neighbor in sorted(graph[node]):  # Sort neighbors lexicographically
            if neighbor not in visited:
                new_path = current_path + [neighbor]
                result = explore_path(new_path, visited | {neighbor})
                if result:  # If a valid path is found
                    lex_paths.append(result)

        return min(lex_paths, key=lambda x: tuple(x)) if lex_paths else None

    # Start exploring from the start node
    visited = {start}
    return explore_path([start], visited)

def main():
    # Create the graph using user input
    G = create_graph()

    # Get start and goal nodes from the user
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    # Perform BMS to find the path
    path = bms_search(G, start, goal)

    if path:
        print(f"Path found: {path}")
    else:
        print("No path found.")

    # Display the graph with the found path highlighted (if any)
    display_graph(G, path)

# Run the main function
if __name__ == "__main__":
    main()
