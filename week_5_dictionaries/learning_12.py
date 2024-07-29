# Sets
# Removes duplicates in a list, 

numbers = [1,1,2,3,4]
uniques = set(numbers)
sets = {1,4}
sets.add(5)
sets.remove(4)


print(numbers)
print(uniques)
print(sets)


# Sets are great for math operations

first = {1,2,3,4}
second = {3,6}

print(first | second) # union - returns unique items of both tables

print(first & second) # intersection - returns items that are in both sets

print(first - second) # difference - returns items that are in the first list but not in the second list

print(first ^ second) # symmetric difference - returns items that are in either set but not both

#Set objects do not support index because it's not ordered

# print(first[0])

# But you can check if an item is in a set
if 3 in first:
  print(True)


# Use Cases:
# Tags for Articles/Posts: When managing tags or categories, sets ensure that 
# each tag is unique and allow for efficient operations on the collection.

#Friends and Connections: Sets are useful for modeling relationships in social 
# networks, such as mutual friends.