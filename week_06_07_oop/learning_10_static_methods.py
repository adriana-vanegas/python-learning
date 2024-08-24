# Static methods
# Methods that can work without needing the self
# it can be used to make a calculation that you want as 
# part of the class (it can live inside or outside of the class)
# i.e. it's semi-related with the class but it's not tied
# to each instance

# vs.
# Class methods are usually used to transfer data from a separate source
# and instantiate it, like a csv, JSON, or yaml file

import csv # to read the csv file

class Item:
  discount_rate = 0.2 
  all = []


  def __init__(self,name: str, price: float, quantity = 0):
    # Run validations
    assert price >= 0, f'Price {price} must be greater than 0' 
    assert quantity >= 0, f'Quantity {quantity} must be greater than 0'

    # Assign instance attributes
    self.name = name  
    self.price = price
    self.quantity = quantity
    Item.all.append(self)
  
  def calculate_price(self):
    cost = self.price * self.quantity
    print(f"Total cost of {self.quantity} {self.name}s is ${cost}")

  def apply_discount(self):
    self.price = self.price * (1 - self.discount_rate)  
    print(f"{self.name} discount price is ${self.price}")

  @staticmethod
  def check_int(num):
    if num.is_integer():
      print(f'{num} is an integer')
    else:
      print(f'{num} is not an integer')


  # Class Method:
  @classmethod # decorators called right before function
  def instantiate_from_csv(cls): # receiving the class itself
    with open('week_6/items.csv','r') as contents: #opens and reads file
      # Converts every row to a dictionary 
      reader = csv.DictReader(contents)
      # Stores every dictionary row into a list to output
      items = list(reader)
      # print(items)

    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = float(item.get('quantity'))
      )

  def __repr__(self):
    return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"
  

Item.check_int(4.0)
Item.check_int(10)
Item.check_int(2.4)