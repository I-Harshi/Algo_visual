import networkx as nx
from Create_graphs import create_graph, display_graph

def bms_search(graph, start, goal):
    all_paths = list(nx.all_simple_paths(graph, source=start, target=goal))

    if not all_paths:
        print(f"No path found from {start} to {goal}.")
        return None


    return all_paths[0]

def main():

    G = create_graph()
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    path = bms_search(G, start, goal)

    if path:
        print(f"Path found: {path}")
    else:
        print("No path found.")

    display_graph(G, path)

if __name__ == "__main__":
    main()
