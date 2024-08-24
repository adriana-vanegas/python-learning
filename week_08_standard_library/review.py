# Classes

class Product:
  product_list = []
  cart = []
  def __init__(self, product_name:str, price:float, size:str):
    self.product_name = product_name
    self.price = price
    self.size = size
    self.product_list.append(self)

  def view_product(self):
    for product in self.product_list:
      print(product)

  def __str__(self):
    return f"{self.product_name}, price: {self.price}, size: {self.size}"


list = [Product('Snake Plant', 15, 'Medium'),
             Product('Maranta', 10, 'Small'),
             Product('Pothos', 25,'Small')
            ]

activate = ''

for item in list:
  activate = item

activate.view_product()


# List Comprehensions

# Extract even values from this list
numbers = [1, 2, 3, 4, 5, 6]

list_comp = [x for x in numbers if x%2 == 0]
print(list_comp)