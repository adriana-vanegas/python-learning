# Dictionary comprehensions



# List Comprehension Example
# Convert this:
values = []

for x in range(5):
  values.append(x * 2)

# Into this:
list_comp = [x * 2 for x in range(5)]

print(list_comp)

# We can do the same for Set
# Set Comprehension
set_comp = {x * 2 for x in range(5)}
print(set_comp)


# What's the difference between a set or a dictionary?
# Dictionaries have key-value pairs
dict = {}

for x in range(5):
  dict[x] = x * 2 # the way to "append" to a dictionary is just by setting the key = value
print(dict)


dict_comp = {x: x * 2 for x in range(5)}
print(dict_comp)