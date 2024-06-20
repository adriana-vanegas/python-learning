# While Loops + If Statement

answer = 9
tries = 1

while tries <= 3:
  guess = int(input("Guess: "))

  if guess == answer:
    print("You got it")
    quit()
  else:
    tries_left = 3 - tries
    print(f"{tries_left} tries left")
    tries += 1
else: 
  print("Game Over")