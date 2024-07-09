import random
from termcolor import colored

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
  rounds_shuffle = list(range(0,num_of_cards))
  random.shuffle(rounds_shuffle)
  correct = 0

  flashcard_tuple = [(word,definition) for word,definition in flashcard.items()]

  for rounds in rounds_shuffle:
    answer = input(colored(f"Capital of {flashcard_tuple[rounds][0]}? ",'blue'))
    if answer.lower() == flashcard_tuple[rounds][1].lower():
      correct += 1
      print(colored("Correct! 💯",'green'))
    else:
      print(colored("Incorrect! 😯",'red'))
      print(f"{flashcard_tuple[rounds][0]} is the capital of {flashcard_tuple[rounds][1]}")

  print(f"Out of {num_of_cards} cards, you got {correct} right")
  quit()
  


def main():
  flashcard = {}
  print(colored("Let's study world capitals 🌏",'yellow'))
  while True:
    print(colored("Enter capital city to study\nView: To view all flashcard\nDelete: To delete a flashcard\nQuiz: To quiz yourself",'blue'))
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