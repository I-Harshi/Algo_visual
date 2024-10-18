from flask import Flask, render_template, request, redirect, url_for, send_file
from BMS import bms_search
from BFS import bfs_search
from DFS import dfs_search
from HC import hill_climbing_search
from Beam import beam_search
from Create_graphs import create_graph, display_graph
import matplotlib as plt
import networkx as nx

app = Flask(__name__)

graph = None
path = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global graph, path

    if request.method == 'POST':

        num_nodes = int(request.form['num_nodes'])
        edges = request.form['edges']
        start = int(request.form['start'])
        goal = int(request.form['goal'])
        algorithm = request.form['algorithm']

        G = nx.Graph()
        for i in range(num_nodes):
            G.add_node(i)

        for edge in edges.splitlines():
            u, v = map(int, edge.split())
            G.add_edge(u, v)

        if algorithm in ['Hill Climbing', 'Beam Search']:
            weights = request.form['weights']
            
            for line in weights.splitlines():
                try:
                    u, v, w = map(int, line.split())
                    G.add_edge(u, v, weight=w)  
                except ValueError:
                    print(f"Invalid weight input: {line}") 
                    return "Invalid weight input. Please provide valid weights."


        if algorithm == 'BMS':
            path = bms_search(G.adj, start, goal)
        elif algorithm == 'BFS':
            path = bfs_search(G, start, goal)
        elif algorithm == 'DFS':
            path = dfs_search(G.adj, start, goal)
        elif algorithm == 'Hill Climbing':
            path = hill_climbing_search(G, start, goal)
        elif algorithm == 'Beam Search':
            path = beam_search(G, start, goal)


        display_graph(G, path)
        plt.savefig('static/graph.png')

        return redirect(url_for('show_graph'))

    return render_template('index.html')

@app.route('/graph')
def show_graph():
    return render_template('graph.html', path=path)

if __name__ == '__main__':
    app.run(debug=True)