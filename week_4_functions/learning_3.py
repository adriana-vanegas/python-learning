# Functions

def greet(first_name,last_name):
  print(f"Hey {first_name} {last_name}!")
  print("Welcome aboard!")


greet("Adriana","Vanegas") #add two line breaks


def get_greeting(name):
  return f"Hi {name}"

message = get_greeting("Adriana")

file = open("week_three/learning_3_get_greeting.txt","w")
file.write(message)

#Use return if you want to display the value
#Use return if you want to send a value from one point in your code to another