from pathlib import Path

path = Path("/Users/avanegas/Documents/GitHub/python-learning/week_8/review.py")

print(path.read_text())

with open(path,"r") as file:
  print(file.read())