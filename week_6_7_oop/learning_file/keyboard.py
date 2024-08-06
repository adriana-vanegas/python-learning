from item import Item

#Keyboard is a child class
class Keyboard(Item): # You can use inheritance through the ()

  discount_rate = 0.1

  def __init__(self,name: str, price: float, quantity = 0, broken_keyboard = 0):
    # Call super function to get access to all 
    # attributes / methods of parent class
    super().__init__(
      name, price, quantity
    )

    # Run validations
    assert broken_keyboard >= 0, f'Broken Phones {broken_keyboard} must be greater than 0'

    # Assign instance attributes
    self.broken_phones = broken_keyboard

  def not_broken(self):
    not_broken_quant = self.quantity - self.broken_phones
    print(f"There are {not_broken_quant} {self.name}s that are not broken")
