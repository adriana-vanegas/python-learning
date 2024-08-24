from item import Item

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
