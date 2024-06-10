import random

from termcolor import colored

from noise import pnoise2

def generate_land(cols=5,rows=15,noise_level=10):
  data = ["⛰","🌲","🌲","🌲","🌳","🏡","🏡","🌳","🌴","🌴","🏖","🌊","🌊","🌊","🌊","🌊","🏖","🌴","🌴","🌳","🏡","🌳","🌲","🌲","🌲","⛰"]

  seed = random.randint(0,500)

  land = ""

  for row in range(rows):

    #row_string = ""
    

    for col in range(cols):

      n = pnoise2(row/rows, col/cols, base = seed, octaves=5) 
      n *= noise_level #likes numbers between 0 and 1
      n = round(n)
      n = n % len(data)
      #print(n)

      #r = random.choice(data)
      land += data[n]
    land += "\n"

  return land
    #print(row_string)

#generate_land(5,5)
#generate_land(10,10)
#generate_land(20) # 20 is used for the first argument


def ask_for_number(question):

  tries = 0
  


  while tries < 3: 
    answer = input(colored(question + "\n","green"))

    if answer.lower() == "quit":
      quit()
    
    elif answer.isnumeric(): 
      return int(answer)
    else: 
      tries_left = 2 - tries
      print(colored(f"The answer needs to be an integer. You have {tries_left} tries left","yellow"))
      tries += 1
  
  print(colored("No tries left","red"))
  quit()

if __name__ == "__main__": # This means that whatever is under here will only run in this file and not in another file that has an import
  cols = ask_for_number("How many columns? ")
  rows = ask_for_number("Now, how many rows? ")

  output = generate_land(cols, rows)

  print(output)