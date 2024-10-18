from flask import Flask, render_template, request, redirect, url_for, send_file
from BMS import bms_search
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

        G = nx.Graph()
        for i in range(num_nodes):
            G.add_node(i)

        for edge in edges.splitlines():
            u, v = map(int, edge.split())
            G.add_edge(u, v)
        path = bms_search(G, start, goal)

        display_graph(G, path)
        plt.savefig('static/graph.png') 

        return redirect(url_for('show_graph'))  

    return render_template('index.html')

@app.route('/graph')
def show_graph():
    return render_template('graph.html', path=path)

if __name__ == '__main__':
    app.run(debug=True)
