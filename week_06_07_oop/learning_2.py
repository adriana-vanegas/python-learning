# Classes: blue print for creating new objects
# Object: instance of a class
# Every object in python is associated with a class

# Example:
# Class: Human
# Object: John, Mary, Jack

#Classes follow the Pascal Naming Conventions 
#   First letter of every word should be upper case
#   No underscores to separate words

class Point:
  def draw(self):
    print("draw")

point = Point()
print(type(point))
print(isinstance(point, Point)) #tests if an object is an instance of the class defined
# i.e. is point an instance of the class MyPoint (it is!)



