#Inheritance
# New Phone class can inherit the structure of the Item class

import csv # to read the csv file


# Item is a parent class
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
    return f"{self.__class__.__name__} name: {self.name}, price: {self.price}, quantity: {self.quantity}"
    # To clarify which class where the instances are coming from,
    # we can print the name of the class 

#Phone is a child class
class Phone(Item): # You can use inheritance through the ()

  def __init__(self,name: str, price: float, quantity = 0, broken_phones = 0):
    # Call super function to get access to all 
    # attributes / methods of parent class
    super().__init__(
      name, price, quantity
    )

    # Run validations
    assert broken_phones >= 0, f'Broken Phones {broken_phones} must be greater than 0'

    # Assign instance attributes
    self.broken_phones = broken_phones

  def not_broken(self):
    not_broken_quant = self.quantity - self.broken_phones
    print(f"There are {not_broken_quant} {self.name}s that are not broken")

# Calculate the # of phones that are not broken
Item.instantiate_from_csv()


phone1 = Phone("iPhone 10", 500, 5,1)

print("Item")
print(Item.all)

print("Phone")
print(Phone.all)
phone1.calculate_price()
phone1.not_broken()