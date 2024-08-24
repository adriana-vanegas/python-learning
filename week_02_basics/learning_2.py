# If Statement 

name = input("What is your first name? ")

if name.isalpha():
  if len(name) < 3:
    print("Name must be at least 3 characters long")
  elif len(name) > 50:
    print("Name can be a max of 50 characters")
  else:
    print(f"Hello {name.capitalize()}")
else:
  print("Name can only have alphabetic values")


weight= input("Weight: ")
metric = input("(L)bs or (K)g: ")

if metric.lower() == "l":
  kilo_conversion = float(weight)*0.45
  print(f"You are {round(kilo_conversion,2)} kg")
else: 
  lbs_conversion = float(weight)*2.2
  print(f"You are {round(lbs_conversion,2)} lbs")
