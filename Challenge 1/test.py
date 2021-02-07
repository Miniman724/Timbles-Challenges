# import json
import json

import time

file = open("actor_by_movie.json", encoding="utf-8")

movie_actor_list = json.load(file)

print(len(movie_actor_list))

list_of_nodes = []

for movie in movie_actor_list:
    list_of_nodes += movie

print(len(list_of_nodes))

dupe_removed_nodes = []

iteration = 0

t0 = time.time()

for actor in list_of_nodes:
    if actor not in dupe_removed_nodes:
        dupe_removed_nodes.append(actor)
    iteration += 1
    if iteration % 50000 == 0:
        print(iteration)
    del actor

t1 = time.time()

total = t1 - t0

print(len(dupe_removed_nodes))
print(total)

processed_actor_file = open("actor_list.json", "w", encoding="utf-8")
json.dump(dupe_removed_nodes, processed_actor_file)
processed_actor_file.close()