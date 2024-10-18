from flask import Flask, render_template, request, redirect, url_for, send_file
from BMS import bms_search
from BFS import bfs_search
from Create_graphs import create_graph, display_graph
import matplotlib as plt
import networkx as nx

app = Flask(__name__)

# Global variables to store the graph and result path
graph = None
path = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global graph, path

    if request.method == 'POST':
        # Get user inputs
        num_nodes = int(request.form['num_nodes'])
        edges = request.form['edges']
        start = int(request.form['start'])
        goal = int(request.form['goal'])
        algorithm = request.form['algorithm']

        # Create the graph
        G = nx.Graph()
        for i in range(num_nodes):
            G.add_node(i)

        for edge in edges.splitlines():
            u, v = map(int, edge.split())
            G.add_edge(u, v)

        # Perform the selected search algorithm
        if algorithm == 'BMS':
            path = bms_search(G.adj, start, goal)  # Use adjacency dict for BMS
        elif algorithm == 'BFS':
            path = bfs_search(G, start, goal)

        # Save the graph image with the highlighted path
        display_graph(G, path)
        plt.savefig('static/graph.png')  # Save in the static folder

        return redirect(url_for('show_graph'))  # Redirect to show graph

    return render_template('index.html')

@app.route('/graph')
def show_graph():
    return render_template('graph.html', path=path)

if __name__ == '__main__':
    app.run(debug=True)
