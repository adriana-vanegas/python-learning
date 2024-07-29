class Item:
    def __init__(self, item_name, item_price, item_quantity=0): # You can set default parameters to arguments
      self.item_name = item_name
      self.item_price = item_price
      self.item_quantity = item_quantity

    def calculate_total(self):  # Methods are functions inside of classes
      # No need to add the "item_name/price" because self already
      # includes all of the values above
      item_total_price = self.item_price * self.item_quantity
      print(f"Total Price of {self.item_name} is ${item_total_price}")

item1 = Item('Phone', '100',4)

item1.calculate_total()

item2 = Item('Laptop', 1000, 2)
item2.has_numberpad = False

item2.calculate_total()