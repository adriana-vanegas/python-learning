import sqlite3
import json
import os

print(os.path.abspath("db.sql"))

# Read the JSON file
with open('week_8/movies.json', 'r') as file_load:
  movies = json.load(file_load)

# Add the JSON file to SQLite DB
# with sqlite3.connect("db.sql") as connection:
#   # Command to create data / add
#   # Question marks represent the values we will add
#   # movies is the name of the table
#   command = "INSERT INTO movies VALUES(?,?)"

#   # To add the values we take out the movies
#   for movie in movies:
#     # We add each value as a tuple
#     connection.execute(command, tuple(movie.values()))

#   # Saves the changes in the database
#   connection.commit()


with sqlite3.connect("db.sql") as connection:
  command = "SELECT * FROM movies"
  # When we pull data, we will get each row (as an iterable)
  cursor = connection.execute(command)
  
  print(cursor.fetchall())

  connection.commit()