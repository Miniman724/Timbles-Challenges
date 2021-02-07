import pickle as pkl

import networkx as nx

# import time for timing processes
import time

# import flask
from flask import Flask, jsonify

# import ast
import ast

# Given an array, it returns every combination of 2 elements from the list
def two_combos(sample_list):
    combo_list = []
    for item1 in sample_list:
        for item2 in sample_list:
            if item1 != item2:
                combo_list.append([item1, item2])
    return combo_list

# Unpickle
t0 = time.time()
graph_file = open("actor_graph.pickle", "rb")
actor_graph = pkl.load(graph_file)
graph_file.close()
t1 = time.time()
print(f"It took {t1 - t0} to load the network")

app = Flask(__name__)

@app.route('/')
def home_page():
    output = "Use /bacon_num/<name> to get bacon number of the actor.\n" \
             "Use /add_movie/{'movie name': ['actor1','actor2'...,'actor n']} to add a movie to the graph."
    return output

@app.route('/bacon_num/<string:name>', methods=['GET'])
def bacon_number(name):
    name = name.replace("_", " ")
    if actor_graph.has_node(name):
        if nx.has_path(actor_graph, source="Kevin Bacon", target=name):
            actor_path = nx.shortest_path(actor_graph, source="Kevin Bacon", target=name)
            for actor in actor_path:
                temp = actor.encode().decode("unicode-escape")
                actor = temp
            degree_of_separation = len(actor_path) - 1
            return jsonify({'path': actor_path, 'bacon_number': degree_of_separation})
        else:
            return f"{name} does not relate to Kevin Bacon"
    else:
        return f"{name} does not exist in the files"

@app.route('/add_movie/<string:new_movie>', methods=['GET', 'POST', 'PUT'])
def add_movie(new_movie):
    print(type(new_movie))
    movie_dict = ast.literal_eval(new_movie)
    print(type(movie_dict))
    movie_list = movie_dict.values()
    print(type(movie_list))
    valid = True
    for movie in movie_list:
        for actor in movie:
            if type(actor) is not str:
                valid = False
    if valid:
        # Get actor list
        actor_set = set([])
        for movie in movie_list:
            actor_set.update(movie)
        actor_set = list(actor)

        # Get edge list
        edge_list = []
        for movie in movie_list:
            edge_list += two_combos(movie)

        # Add new nodes and edges
        actor_graph.add_nodes_from(actor_set)
        actor_graph.add_edges_from(edge_list)

        return f"Added {movie_list}"

    else:
        return "The entry is invalid"

