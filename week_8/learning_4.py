# Paths

import os

print("This is the file path")
# Returns the absolute path of a file
print(os.path.abspath("learning_4.py"))

# Make directories
os.makedirs("week_8/new_directory", exist_ok=True)

# Create a new file
with open('week_8/new_directory/myfile.txt','w') as fp:
  pass

with open('week_8/new_directory/myfile_to_delete.txt','w') as fp:
  pass

# Remove a file
os.remove('week_8/new_directory/myfile_to_delete.txt')
