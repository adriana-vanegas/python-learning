# Looping over lists

# Print items in list with the index
list = ['a','b','c']

print(enumerate(list))

for index, letter in enumerate(list):
  print(index, letter)

# Tuples are read-only, new items can't be added

