from random import choice

def randomfunfact():
  funfacts = ["Kansas is considered flat","Wichita is the biggest city","Kansas City is mostly in Missouri"]
  print(choice(funfacts))

# Works to only run the randomfunfact in this sheet
# Not if it's imported, yet not called in another sheet
if __name__ == "__main__":
  randomfunfact()