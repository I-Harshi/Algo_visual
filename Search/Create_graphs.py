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
def display_g(G, path, algorithm, cost):
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2)

    title = f"{algorithm} | Cost: {cost if cost is not None else 'N/A'}"
    plt.title(title, fontsize=15)
    plt.show()