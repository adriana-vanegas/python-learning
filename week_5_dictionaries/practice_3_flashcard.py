def add_card(flashcard,new_word):
  definition = input(f"{new_word} is the capital of: ")
  flashcard[new_word] = definition


def view_card(flashcard):
  print("Flashcards:")
  for key_item in flashcard.items():
    print(f"{key_item[0]}: {key_item[1]}")

def delete_card(flashcard):
  remove_word = input(f"Flashcard to remove: ")
  if remove_word in flashcard:
    del flashcard[remove_word]
    print(f"{remove_word} is removed from deck")
  else:
    print(f"{remove_word} is not in deck.")
    view_card(flashcard)

def quiz(flashcard):
  print("Let's quiz you 🧐")
  num_of_cards = len(flashcard)
  rounds = 0
  correct = 0

  flashcard_tuple = [(word,definition) for word,definition in flashcard.items()]

  while rounds < num_of_cards:
    answer = input(f"Capital of {flashcard_tuple[rounds][0]}? ")
    if answer.lower() == flashcard_tuple[rounds][1].lower():
      correct += 1
      print("Correct!")
    else:
      print("Incorrect!")
      print(f"{flashcard_tuple[rounds][0]}'s capital is {flashcard_tuple[rounds][1]}")
    rounds += 1

  print(f"Out of {num_of_cards} cards, you got {correct} right")
  quit()
  


def main():
  flashcard = {}
  print("Let's start studying 📚")
  while True:
    print("Write any word to study\nView: To view all flashcard\nDelete: To delete a flashcard\nQuiz: To quiz yourself")
    action = input("> ")
    if action.lower() == 'view':
      view_card(flashcard)
    elif action.lower() == 'delete':
      delete_card(flashcard)
    elif action.lower() == 'quiz':
      quiz(flashcard)
    else:
      add_card(flashcard,action)


main()