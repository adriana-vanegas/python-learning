  # READ ONLY ATTRIBUTE 
  # i.e. Set a value that can't be changed
  

import csv


class Item:
  discount_rate = 0.2 
  all = []


  def __init__(self,name: str, price: float, quantity = 0):
    assert price >= 0, f'Price {price} must be greater than 0' 
    assert quantity >= 0, f'Quantity {quantity} must be greater than 0'

    # Since the property can't be set, you need to add
    # an underscore or double  before the attribute name
    self.__name = name  
    self.price = price
    self.quantity = quantity

    Item.all.append(self)

  # Property decorate = Read only attribute
  # Also add the underscore before the attribute
  @property
  def name(self):
    return self.__name
  
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


  @classmethod 
  def instantiate_from_csv(cls): 
    with open('week_6/learning_file/items.csv','r') as contents: 
      reader = csv.DictReader(contents)
      items = list(reader)

    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = float(item.get('quantity'))
      )

  def __repr__(self):
    return f"{self.__class__.__name__} name: {self.name}, price: {self.price}, quantity: {self.quantity}"
  

  # Encapsulation: 
# Set the name of a value that cannot be overriden
item1 = Item("Sound Bar",400)
item1.name
print(item1.name)
