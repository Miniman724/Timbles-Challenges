# Outputs a file of form:
# [[actors from movie 1], [actors from movie 2], ... [actors from movie n]]

# import csv
import csv

# import ast
import ast

# import json
import json

# Open File
csv_file = open("credits.csv", encoding="utf-8", newline='')
reader = csv.reader(csv_file)

# Put everything from the first column into an array
cast_list = []
for row in reader:
    cast_list.append(row[0])
del cast_list[0]
csv_file.close()

print("finished reading file")

# Convert the strings to dictionaries and store them in a new array
modified_cast_list = []
for element in cast_list:
    temp = ast.literal_eval(element)
    modified_cast_list.append(temp)
del cast_list

print("converted strings to lists")

# Extract a list of the actors from each movie and store them in a nested array
# (Array of list of actors in movies)
actor_list = []
for element in modified_cast_list:
    movie_actors = []
    for actor in element:
        movie_actors.append(actor["name"])
    actor_list.append(movie_actors)

print("extracted names, now outputing file")

# Output the file
processed_actor_file = open("actor_by_movie.json", "w", encoding="utf-8")
json.dump(actor_list, processed_actor_file)
processed_actor_file.close()

