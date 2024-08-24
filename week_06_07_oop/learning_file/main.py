from item import Item
from phone import Phone
from keyboard import Keyboard

# Encapsulation: 
# Set the value of an instance cannot be overriden
# Instead they can be adjusted through setters or by 
# recalculating new values
# item1 = Phone("Sound Bar",400,6)
item1 = Keyboard('Mega Keys',300)
print(item1.price)
# item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

# Abstraction:
# Only shows necessary attributes
# item1.send_email() # sending an email requires many steps
# but not all of them should be shown

# Inheritance:
# Allows us to reuse parent code across all child classes

# Polymorphism
# A single entity that can be used from multiple objects
# For example, we can use the Phone class and have it pass 
# through the apply_discount method