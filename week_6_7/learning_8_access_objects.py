# Access all objects in the class

# Create a list within the class item and append 
# each item within def __init__


# Using __repr__ to change how the Item.all is outputted

class Item:
  discount_rate = 0.2 # Full store discount

  all = [] 

  def __init__(self,name: str, price: float, quantity = 0):
    # Run validations
    assert price >= 0, f'Price {price} must be greater than 0' 
    assert quantity >= 0, f'Quantity {quantity} must be greater than 0'

    # Assign instance attributes
    self.name = name  # Instance attributes
    self.price = price
    self.quantity = quantity

    # Actions to execute
    Item.all.append(self) 

  
  def calculate_price(self):
    cost = self.price * self.quantity
    print(f"Total cost of {self.quantity} {self.name}s is ${cost}")

  def apply_discount(self):
    self.price = self.price * (1 - self.discount_rate)  
    print(f"{self.name} discount price is ${self.price}")

  def __repr__(self): #represent magic method
    return f"Item('{self.name}','{self.price}','{self.quantity}')"
  

item1 = Item('Phone', 100, 1) 
item2 = Item('Laptop', 1000, 4)
item3 = Item('Cable', 10,5)
item4 = Item('Mouse', 50,2)
item5 = Item('Keyboard', 75,3)


print(Item.all)

for item in Item.all:
  print(item.name)

