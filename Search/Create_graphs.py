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


    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_size=15, font_color='black', edge_color='gray')
    plt.show()