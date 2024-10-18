import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    num_nodes = int(input("Enter the number of nodes: "))
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    num_edges = int(input(f"Enter the number of edges (connections) for {num_nodes} nodes: "))

    print("Enter the connections (e.g., 0 1 to connect node 0 and 1):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        G.add_edge(u, v)

    return G

def display_graph(G, path=None):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)


    if path:
        edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=15)
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)
    else:
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=15, edge_color='gray')

    plt.show()
