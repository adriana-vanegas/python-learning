import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5])) # randomly chooses from array
print(random.choices([1,2,3,4,5],k=2)) # randomly chooses multiple values from array


# Random password generator:

# Join joins all of the items in the list from the choices output
# and the "" (is the separator), there's no space in between the random choices
print("".join(random.choices(string.ascii_letters + string.digits + string.punctuation,k=9)))

#Reorder of numbers
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)