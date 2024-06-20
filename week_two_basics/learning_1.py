#If Statement

temperature = 'not hot or cold'

# a single = is kind of like "setting a variable"
# a double == is like "does it equal to x?"

if temperature.lower() == 'hot':
  print("It's a hot day. \n Drink plenty of water")
elif temperature.lower() == 'cold':
  print("It's a cold day. \n Wear warm clothes")
else:
  print("It's a lovely day")

credit = input("What is your credit score? ")
income = input("What is your annual income? ")

if int(credit) > 650 or int(income)>50000:
  print("You are eligible for a loan")
else: 
  print("You are not eligible for a loan")

good_credit = True
has_criminal_record = True

if good_credit and not has_criminal_record:
  print("Eligible")