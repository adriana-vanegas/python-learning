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

print(first | second) # union | 

print(first & second) # returns items that are in both sets

print(first - second) #returns items that are not in both sets

print(first ^ second) # retunrs items that are in either set but not both

#Set objects do not support index because it's not ordered

# print(first[0])

# But you can check if an item is in a set
if 3 in first:
  print(True)