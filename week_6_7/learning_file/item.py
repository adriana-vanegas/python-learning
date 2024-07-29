
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
    self.__price = price
    self.quantity = quantity

    Item.all.append(self)

  @property
  def price(self):
    return self.__price

  # Property decorate = Read only attribute
  # Also add the underscore before the attribute
  @property
  def name(self):
    return self.__name
  
  #if you want to change the value of a read only attribute
  # you would need to use a setter
  @name.setter
  def name(self, new_val_name): # new_val_name is the value that will replace the __name
    if len(new_val_name)>10:
      raise Exception("name is too long")
    else:
      self.__name = new_val_name

  
  
  def calculate_price(self):
    cost = self.__price * self.quantity
    print(f"Total cost of {self.quantity} {self.name}s is ${cost}")

  def apply_discount(self):
    self.__price = self.__price * (1 - self.discount_rate)  
    print(f"{self.name} discount price is ${self.__price}")
  
  def apply_increment(self,increment):
    self.__price = self.__price + (self.__price * increment)

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
      # print(items)
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = float(item.get('quantity'))
      )

  def __repr__(self):
    return f"{self.__class__.__name__} name: {self.name}, price: {self.__price}, quantity: {self.quantity}"
  

