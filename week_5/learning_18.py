## All the things I'm confused about
## Zip
## Sort dictionaries
## Sorting and filtering exercises
## Dictionary indexing
## Unpacking Dictionaries

# Zip 
# Zip objects are great to aggregate elements of 2+ iterables and stores them in a tuple

usernames = ['adriana','realadri','paco']
password = ['password','wordpass','pet']

# Combining the two lists
users = zip(usernames,password)

# To view all values in a zip object, you have to take them out one by one using a for loop
print([i for i in users])


# We can convert zip objects to a list or a tuple or a dictionary
users_list = list(zip(usernames,password))
print(users_list)
users_tuple = tuple(zip(usernames,password))
print(users_tuple)
users_set = set(zip(usernames,password))
print(users_set)
users_dict = dict(zip(usernames,password))
print(users_dict)



# If there's an uneven amount of values inside of the lists to zip,
# the output will only contain the values that have pairs and exclude the extra values that don't have a pair

username_uneven = ['adriana','realadri']
password_uneven = ['password','wordpass','pet']

users_uneven = zip(username_uneven,password_uneven)

print([i for i in users_uneven])


# Example 2:


names = ['Claire','Mario','Pete','Pooja']
age = [23,18,27,24]

zip_names = (zip(names,age))

for name,age in zip_names:
  print(f"Name : {name}, Age: {age}")

for i in zip_names:
  print(i)


#Example 3

sales = [500,800,300,1200,600]
costs = [200,600,200,800,700]

# Get the profits
print([rev - cost for rev, cost in zip(sales,costs)])


# Example 4.a: Unzipping
zipped = [('Mike',50),('Bob',20),('Anna',70),('Kate',30)]

names, ages = zip(*zipped)
print(names)
print(ages)


# Example 4.b: Unzipping dictionaries
zipped_dict = {'Mike':50,'Bob':20,'Anna':70,'Kate':30}
name_dict, age_dict = zip(*zipped_dict.items())
print(name_dict)
print(age_dict)

# Example 5: 

letters = ['b','d','a','c']
numbers = [3,4,1,2]

letters.sort()
numbers.sort()

print(list(zip(letters,numbers)))

