#Debugging

#Initial code with a bug:
def multiply(*numbers):
  total = 1
  for i in numbers:
    total *= i
  return total

print("Start")
print(multiply(1,2,3))
# output is 1 because the return stops the for loop after the first iteration (i.e. 1)

#Debugging Keys
# F5 to start debugging
# F9 to toggle a breakpoint (i.e. stop the execution at a specific line)
# F10 steps over to the next line for debugging
# F11 steps into