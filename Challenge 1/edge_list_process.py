# import json
import json

# import time for timing
import time

# Given an array, it returns every combination of 2 elements from the list
def two_combos(sample_list):
    combo_list = []
    for item1 in sample_list:
        for item2 in sample_list:
            if item1 != item2:
                combo_list.append([item1, item2])
    return combo_list

# Open file
file = open("actor_by_movie.json", encoding="utf-8")
movie_actor_list = json.load(file)

# Combine every single combination of actors from every movie
t0 = time.time()
edge_set = []
for movie in movie_actor_list:
    edge_set += two_combos(movie)
t1 = time.time()
print(f"It took {t1 - t0} seconds to combine every single combination of actors from every movie")

# Outputting file
print("Outputting file.")
processed_actor_file = open("edge_list.json", "w", encoding="utf-8")
json.dump(edge_set, processed_actor_file)
processed_actor_file.close()