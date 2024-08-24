# Shopping Cart
from termcolor import colored

def is_integer(value_check):
  value_check = value_check.replace('.','')
  if value_check.isdigit():
    return True
  else:
    return False

def add_item(cart,item_name):
  check_off = True
  while check_off == True:
    item_price = input("Item price: $")
    item_quantity = input(f"Quantity: ")
    if is_integer(item_price) and is_integer(item_quantity):
      cart[item_name]= {'price': item_price, 'quantity': item_quantity}
      check_off = False
    else:
      print("Only enter numerical values")


def del_item(cart):
  item_to_remove = input("What item do you want to remove? ")
  if item_to_remove in cart:
    del cart[item_to_remove]
  else:
    print('Item is not in cart. See items in cart:')
    view_item(cart)


def done_item(cart):
  total = 0
  total_item_amount = 0
  for product in cart.items():
    price = product[1]['price']
    quantity = product[1]['quantity']
    total += (float(price) * float(quantity))
    total_item_amount += int(quantity)
  total_plus_tax = total*1.07
  print(colored("Thank you for your purchase!",'magenta'))
  view_item(cart)
  print(colored(f"Total cost + tax: ${total_plus_tax:.2f}",'green'))
  quit()


def view_item(cart):
  ordered_cart = sorted(cart.items(), key = lambda list:list[1]['quantity'])
  for product in ordered_cart:
    print(f"{product[1]['quantity']} {product[0]} for ${product[1]['price']}")
  

def main():
  print(colored("Let's get groceries! 🛒","light_yellow"))
  cart = {}
  
  while True:
    print(colored("Write item name to add item","blue"))
    print(colored("'remove' to remove item from cart","blue"))
    print(colored("'view' to view cart","blue"))
    print(colored("'done' to check out","blue"))
    action = input("> ")
    if action.lower() == 'remove':
      del_item(cart)
    elif action.lower() == 'view':
      view_item(cart)
    elif action.lower() == 'done':
      done_item(cart)
    else: 
      add_item(cart,action)

main()

