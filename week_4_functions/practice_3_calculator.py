def calculation(starting_value):
  accurate = False
  while accurate == False:
    print("Choose action: \n   +: Add \n   -: Subtract \n   *: Multiply \n   /: Divide \n   Q: Quit")
    action = input("> ")
    if action.lower() == '+':
      add(starting_value)
    elif action.lower() == '-':
      subtract(starting_value)
    elif action.lower() == '*':
      multiply(starting_value)
    elif action.lower() == '/':
      divide(starting_value)
    elif action.lower() == 'q':
      print(f'End Result = {starting_value}')
      quit()
    else:
      print('You must choose one of the following actions.')
    

def add(starting_val):
  add_value = input(f'{starting_val} + ')
  new_value = int(starting_val) + int(add_value)
  print(f'Result = {new_value}')
  calculation(new_value)


def subtract(starting_val):
  sub_value = input(f'{starting_val} - ')
  new_value = int(starting_val) - int(sub_value)
  print(f'Result = {new_value}')
  calculation(new_value)


def multiply(starting_val):
  mult_value = input(f'{starting_val} * ')
  new_value = int(starting_val) * int(mult_value)
  print(f'Result = {new_value}')
  calculation(new_value)


def divide(starting_val):
  div_value = input(f'{starting_val} / ')
  new_value = int(starting_val) / int(div_value)
  print(f'Result = {new_value}')
  calculation(new_value)


def start():
  starting_value = input("> ")
  calculation(starting_value)


start()