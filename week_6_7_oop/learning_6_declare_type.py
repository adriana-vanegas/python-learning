# Declare Typings
# You can declare an instance variable to a specific type like float, str, int, etc.

# Running validations by using assert to validate the arguments given

class Item:
  def __init__(self,name: str, price: float, quantity = 0):
    # quantity is already an integer because it's set to 0, an integer

    #Run validations to the received arguments
    assert price >= 0, f'Price {price} must be greater than 0' 
    assert quantity >= 0, f'Quantity {quantity} must be greater than 0'
    # assert statement used to check if there's a match
    # after comma, you can write desired error message


    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

  
  def calculate_price(self):
    cost = self.price * self.quantity
    print(f"Total cost of {self.quantity} {self.name}s is ${cost}")

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 4)

item1.calculate_price()
item2.calculate_price()