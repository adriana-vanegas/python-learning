#For Loops

# Loops iterate over items in a collection
# Loop variable: in each iteration, the variable will hold 1 item
# Collection: A collection can be a string, or a list [1,2,3], or a range () for a range of numbers
# In a range you can have (min, max, step function)

prices = [10,20,30]
total = 0

for item in prices:
  total += item
print(total)
