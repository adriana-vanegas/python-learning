# JSON
import json
import os

movies = [
  {"title": "The Proposal", "year":2012},
  {"title": "John Tucket Must Die", "year":2006}
]


# DUMP = Writes data to a file in a JSON format
with open('week_8_standard_library/movies.json','w') as file_json:
  json.dump(movies,file_json)

# LOAD = Reads a JSON file
with open('week_8_standard_library/movies.json','r') as file_read:
  movie_list = json.loads(file_read.read())
  print(movie_list)

for i in movie_list:
  print(i['title'])