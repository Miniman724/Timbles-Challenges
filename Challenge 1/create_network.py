# Outputs a network x graph using pickle

# import json
import json

# import time
import time

# import networkx
import networkx as nx

# import pickle
import pickle

# Load Nodes
print("Loading Nodes")
node_file = open("actor_list.json", encoding="utf-8")
node_list = json.load(node_file)
print("Done")

# Load Edges
print("Loading Edges")
edge_file = open("edge_list.json", encoding="utf-8")
edge_list = json.load(edge_file)
print("Done")

# Create graph object
actor_graph = nx.Graph()

print("Start")

# Unescape unicode escaped nodes
t0 = time.time()
for item in node_list:
    temp = item.encode().decode("unicode-escape")
    item = temp
t1 = time.time()
print(f"Time to unescape nodes: {t1 - t0}")

# Add nodes
t0 = time.time()
actor_graph.add_nodes_from(node_list)
t1 = time.time()
print(f"Time to add nodes: {t1 - t0}")

# Unescape unicode escaped edges
t0 = time.time()
for item in node_list:
    for actor in item:
        temp = item.encode().decode("unicode-escape")
        actor = temp
t1 = time.time()
print(f"Time to unescape edges: {t1 - t0}")

# Add edges
t0 = time.time()
actor_graph.add_edges_from(edge_list)
t1 = time.time()
print(f"Time to add edges: {t1 - t0}")

# Pickle the object
t0 = time.time()
graph_file = open("actor_graph.pickle", "wb")
pickle.dump(actor_graph, graph_file)
graph_file.close()
t1 = time.time()
print(f"Time to pickle: {t1 - t0}")

# Check if unicode worked
if actor_graph.has_node("Elina Löwensohn") == False:
    print("UNICODE FAILED")