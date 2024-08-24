import re

def main(text):
  # Remove punctuation and set all words into lower
  new_text = re.sub(r'[^\w\s-]','',text)

  words = new_text.split()
  # Split removes all whitespaces, new lines, etc

  # Count the total number of words.
  word_count = len(words) # Number of Characters


  # Identify and count the unique words 
  set_build = set(words)
  # print(set_build)


  # Frequency of each word:
  dictionary = {}
  for key in set_build:
    dictionary[key] = 0

  for key in words:
    dictionary[key] += 1


  # Order from largest to smallest
  ordered = sorted(dictionary.items(), key = lambda val:val[1], reverse = 'True')

  # Find the longest and shortest words
  longest_word = max(set_build,key = len)
  shortest_word = min(set_build,key = len)


  print(f"Total # of words: {word_count}")
  print(f"Total # of unique words: {len(set_build)}")
  print(f"Most frequently used words: {ordered[0][0].capitalize()} used {ordered[0][1]} times")
  print(f"Longest word: {longest_word}")
  print(f"Shortest word: {shortest_word}")


text_value = input("Enter text to analyze\n")
main(text_value)