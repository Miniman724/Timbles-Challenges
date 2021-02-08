# Timbles-Challenges
Challenges from Timbles

# Challenge 1:
Processing:
1. Run data_process.py in the same directory as credits.csv. This creates a list containing list of actors in a movie stored in actor_by_movie.json
2. Run actor_list_process.py. This creates a list of all the actors without any duplicates stored in actor_list.json
3. Run edge_list_process.py. This creates a list of all connections between actors in movies. This is stored in edge_list.json
4. Run create_network.py. This creates a Network X object that graphs the actors and connections, using actor_list as the nodes and edge_list as the edges
5. We now have an graph object that is pickled into actor_graph.pickle

Running the Service:
Run the Flask App, called app.py

# Challenge 2:
Run SalesTaxes.py.
You are able to enter manually or by txt file.

# Demonstrations:
In each folder, I have included some screenshots of the results of the programs.

# NOTES
1. There is a typo in the picture for "4 create network results.png". It says that 2 nodes are added twice, but one was adding edges.
2. To add a movie, you would put the dictionary value like so: /add_movie/{"movie_name",["actor 1","actor 2"]}
