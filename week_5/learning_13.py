# Dictionaries
# Collection of key-value pairs
# For example, a phone book matches a person's name (key) to their contact detail

# Two ways to make a dictionary
method1 = {"x":1,"y":2}

method2 = dict(x=1, y=2)

method3 = {1:'x', 2:'x'} #We can also have numbers as the key

# To index a dictionary, you have to call it by its key name
print(method1['x'])
print(method3[1])

# To change values
method2['x']=10
print(method2)

# To add more key-value pairings
method2['z']=20
print(method2)

# To check for existence of a key:
if 'a' in method2:
  print(method2['a'])

# or use the "get" method
print(method2.get('x',0)) #gets the value of the key if available, else 0

# To delete a statement
del method2['x']
print(method2)

# To loop over dictionaries
for key in method2:
  print(key, method2[key])

#The loop only prints the key of the dictionary

# Or we can get tuples of the item
for x in method2.items():
  print(x)

# Or we can unpack the tuples
for key,value in method2.items():
  print(key, value)

