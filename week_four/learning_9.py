# Enumerate
# Best source: https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python

values = ['first', 'second','third']

# Sets the number to each value
enumerated_list = enumerate(values)

# Creates a list of the enumerated values
valueslist = list(enumerated_list)

print(valueslist)

###############

groceries = ['milk','eggs','jam']

for index,i in enumerate(groceries, start = 1):
  print(f'{index} {i}')

# index let's you get the index value of the item in the list