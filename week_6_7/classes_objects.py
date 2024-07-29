# Objects are a collection of variables and functions
# Object can represent a person or a user or anything


#Variables within an object are called instance variables or attributes
# Functions within an object are called methods

# Classes are a blueprint from which you can make objects

# Constructors let's you set variables to an object (aka instance variables/attributes)

class Robot:
  def __init__(self, name, color, weight): # init let's you create a constructor
    self.name = name  #set the object's name = name_val
    self.color = color
    self.weight = weight

    
  def introduce_self(self):  
    # when a function is within a class (it becomes a method of the class)
    # which means it has to have a self argument
    print(f"Hello, I am {self.name}")


#Version 1:

# r1 = Robot()
# # Set the object's attributes
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r1.introduce_self()  # self will refer to r1


# r2 = Robot()
# r2.name = "Jerry"
# r2.color = 'blue'
# r2.weight = 40

# r2.introduce_self()  # self will refer to r1


#Version 2
r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue",40)

r1.introduce_self()
r2.introduce_self()