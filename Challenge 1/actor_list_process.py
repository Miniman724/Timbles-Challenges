# Outputs a file of form:
# [actor 1, actor 2, actor 3 ... actor n] in which there are no duplicate actors

# import json
import json

# import time for timing processes
import time

# Open file
file = open("actor_by_movie.json", encoding="utf-8")
movie_actor_list = json.load(file)
print(f"There are {len(movie_actor_list)} movies in the list")


# Combine and remove duplicates
t0 = time.time()
actor_set = set([])
for movie in movie_actor_list:
    actor_set.update(movie)
t1 = time.time()
print(f"It took {t1 - t0} seconds to combine and remove duplicates")
output = list(actor_set)
print(f"There are {len(output)} actors")

print("Outputting file.")
processed_actor_file = open("actor_list.json", "w", encoding="utf-8")
json.dump(output, processed_actor_file)
processed_actor_file.close()