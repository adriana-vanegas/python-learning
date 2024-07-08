##################
# List Unpacking #
##################

# Example 1:
list = ['apple','orange','potato','celery']

fruit_1, fruit_2, veggie_1, veggie_2 = list

print(fruit_1)
print(fruit_2)
print(veggie_1)
print(veggie_2)

# Example 2:
list_2 = ['beach','umbrella','towel','fish']

location, *packing_list, food = list_2

print(location)
print(packing_list)
print(food)

# Example 3: You can also unpack items in a for loop:

list_3 = [['a','b'],
          ['c','d'],
          ['e','f'],
          ]

for first, last in list_3:
  print(first, last)



################
# List Slicing #
################

# Example 1: Skip over 2 
print(list_2[1::2])

# Example 2: print in reverse order
print(list_2[::-1])

# reverse() only works for numbers in a string
list_2.reverse()
print(list_2)

