a = 12
b = 4

print("Calculation Menu\n+ to Add\n- to Subtract\n* to Multiply\n/ to Divide")

question = input("Choose your calculation: ")

if question == '+':
  result = a + b
  print(f"{a} + {b} = {result}")
elif question == '-':
  result = a - b
  print(f"{a} - {b} = {result}")
elif question == '*':
  result = a * b
  print(f"{a} * {b} = {result}")
elif question == '/':
  result = a / b
  print(f"{a} / {b} = {result}")
else:
  print("Invalid calculation option")