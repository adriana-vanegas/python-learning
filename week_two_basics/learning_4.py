# While Loops + If Statement

tries = 0
max_tries = 3
current_year = 2024


while tries < max_tries:
  birth_year = input("What is your birth year? ")

  if birth_year.isnumeric():
    age = current_year - int(birth_year)
    print(f"You are {age} years old.")
    quit()
  else:
    tries += 1
    remaining_tries = max_tries - tries
    print(f"You have {remaining_tries} tries left")
quit()
  
