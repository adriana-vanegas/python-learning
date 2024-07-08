flashcard = {'George Washington':'First president','Abraham Lincoln': '16th president'}

num_of_cards = len(flashcard)
print(num_of_cards)

rounds = 0
correct = 0

flashcard_tuple = [(word,definition) for word,definition in flashcard.items()]

while rounds < num_of_cards:
  answer = input(f"Who is {flashcard_tuple[rounds][0]}? ")
  print(rounds)
  if answer.lower() == flashcard_tuple[rounds][1].lower():
    correct += 1
    print("Correct!")
  else:
    print("Incorrect!")
    print(f"{flashcard_tuple[rounds][0]} is {flashcard_tuple[rounds][1]}")
  rounds += 1

print(f"Out of {num_of_cards} cards, you got {correct} right")