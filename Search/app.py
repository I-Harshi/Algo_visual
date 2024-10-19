from flask import Flask, render_template, request, redirect, url_for
from BMS import bms_search
from BFS import bfs_search
from DFS import dfs_search
from HC import hill_climbing_search
from Beam import beam_search
from bnb_heu import branch_and_bound_heuristics
from bnb_list import branch_and_bound_with_extension
from branch_and_bound import branch_and_bound
from branch_and_bound import branch_and_bound
from A_star import a_star_search
from oracle import oracle_search
from best_first import best_first_search
from Create_graphs import create_graph, display_g
import matplotlib.pyplot as plt
import networkx as nx

app = Flask(__name__)

graph = None
path = None
cost = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global graph, path, cost

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

        if algorithm not in ['BMS', 'BFS', 'DFS']:
            weights = request.form['weights']
            for line in weights.splitlines():
                try:
                    u, v, w = map(int, line.split())
                    G.add_edge(u, v, weight=w)
                except ValueError:
                    return "Invalid weight input. Please provide valid weights."

        if algorithm == 'BMS':
            path = bms_search(G.adj, start, goal)
            cost = None
        elif algorithm == 'BFS':
            path = bfs_search(G, start, goal)
            cost = None
        elif algorithm == 'DFS':
            path = dfs_search(G.adj, start, goal)
            cost = None
        elif algorithm == 'Hill Climbing':
            path = hill_climbing_search(G, start, goal)
            cost = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
        elif algorithm == 'Beam Search':
            path, cost = beam_search(G, start, goal)
        elif algorithm == 'Branch and Bound':
            path, cost = branch_and_bound(G, start, goal)
        elif algorithm == 'Branch and Bound with Heuristics':
            heuristics_input = request.form['heuristics']
            heuristic = {int(node): int(value) for node, value in 
                        [line.split() for line in heuristics_input.splitlines()]}
            path, cost = branch_and_bound_heuristics(G, start, goal, heuristic)
        elif algorithm == 'Branch and Bound with Extended List':
            heuristics_input = request.form['heuristics']
            heuristic = {int(node): int(value) for node, value in 
                        [line.split() for line in heuristics_input.splitlines()]}
            path, cost = branch_and_bound_with_extension(G, start, goal, heuristic)
        elif algorithm == 'A* Search':
            heuristics_input = request.form['heuristics']
            heuristic = {int(node): int(value) for node, value in 
                        [line.split() for line in heuristics_input.splitlines()]}
            path, cost = a_star_search(G, start, goal, heuristic)
        elif algorithm == 'Oracle Search':
            heuristics_input = request.form['heuristics']
            heuristic = {int(node): int(value) for node, value in 
                        [line.split() for line in heuristics_input.splitlines()]}
            path, cost = oracle_search(G, start, goal, heuristic)
        elif algorithm == 'Best First Search':
            heuristics_input = request.form['heuristics']
            heuristic = {int(node): int(value) for node, value in 
                        [line.split() for line in heuristics_input.splitlines()]}
            path, cost = best_first_search(G, start, goal, heuristic)

        display_g(G, path, algorithm, cost)
        plt.savefig('static/graph.png')

        return redirect(url_for('show_graph'))

    return render_template('index.html')

@app.route('/graph')
def show_graph():
    return render_template('graph.html', path=path, cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
