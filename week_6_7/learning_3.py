class User:
  default_color = 'red' # Class attribute (default across the class)
  # it's not super common to have class-level attributes.
  # Instance variables are more common

  def __init__(self, name, gender): #Instance variables that can vary by object
    self.name = name 
    self.gender = gender

  def call_name(self): # This is an instance method
    print(f"Hey {self.name}")

######################

# Instance Variables #

######################

# The User object will always have the instance variables by default
# But you can keep adding more afterwards
user1 = User('Manny', 'Female')
user1.hobby = 'Coding'
print(user1.gender)
user1.call_name()

user2 = User('John', 'male')

###################

# Class Variables #

###################

# The class variable for an object, but it won't change the other objects
user1.default_color = "yellow"
print(user1.default_color)
print(user2.default_color)


# If you change the class variable for the class itself, it will 
# change for all objects, unless an object has redefined the default
User.default_color = 'green'
print(user1.default_color)
print(user2.default_color)


###################

# Class Functions #

###################




# Test of prior learnings:

# dict = {'user1':5, 'user2':8, 'user3':10}

# ordered_dict = list(sorted(dict.items(), key = lambda user:user[1]))
# print(ordered_dict)
