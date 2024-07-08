# Shopping Cart
from termcolor import colored

def add_item(cart,item_name):
  item_price = input("What's the individual price? $")
  item_quantity = input(f"How many {item_name}? ")
  cart[item_name]= {'price': item_price, 'quantity': item_quantity}


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
    product_name = product[0]
    price = product[1]['price']
    quantity = product[1]['quantity']
    print(f"{quantity} {product_name} for ${price} each.")
    total += (int(price) * int(quantity))
    total_item_amount += int(quantity)
  average = total/total_item_amount
  print(f"Total cost: ${total:.2f} and average cost per item:${average:.2f}")
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
    print(colored("'del' to remove item","blue"))
    print(colored("'view' to view list","blue"))
    print(colored("'done' to check out","blue"))
    action = input("> ")
    if action.lower() == 'del':
      del_item(cart)
    elif action.lower() == 'view':
      view_item(cart)
    elif action.lower() == 'done':
      done_item(cart)
    else: 
      add_item(cart,action)

main()