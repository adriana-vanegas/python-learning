# Global class attributes
# Class attribute will belong to the class itself

# How to see attributes at the class and instance level

class Item:
  discount_rate = 0.2 # Full store discount

  def __init__(self,name: str, price: float, quantity = 0):
    assert price >= 0, f'Price {price} must be greater than 0' 
    assert quantity >= 0, f'Quantity {quantity} must be greater than 0'
    self.name = name  # Instance attributes
    self.price = price
    self.quantity = quantity

  
  def calculate_price(self):
    cost = self.price * self.quantity
    print(f"Total cost of {self.quantity} {self.name}s is ${cost}")

  def apply_discount(self):
    self.price = self.price * (1 - self.discount_rate)  
    print(f"{self.name} discount price is ${self.price}")

item1 = Item('Phone', 100, 1) 
item2 = Item('Laptop', 1000, 4)


print(Item.discount_rate)
print(item1.discount_rate)
print(item2.discount_rate)


# To see all attributes for class level
print(Item.__dict__) # magic method converts everything into a dictionary

# To see all attributes for the instance level
print(item2.__dict__)

# To have a 30% discount for a specific object
item2.discount_rate = 0.3
item1.apply_discount()
item2.apply_discount()
