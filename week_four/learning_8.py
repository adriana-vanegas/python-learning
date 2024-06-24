# def fizz_buzz(*input):
#   for i in input:
#     if i%3 ==0 and i%5 == 0:
#       print(f"{i} Fizz Buzz")
#     elif i%3 == 0:
#       print(f"{i} Fizz")
#     elif i%5 == 0:
#       print(f"{i} Buzz")
#     else:
#       print(i)

# fizz_buzz(3,10,15,7)


def fizz_buzz(i):
  if (i%3 ==0) and (i%5 == 0):
    return "Fizz Buzz"
  if i%3 == 0:
    return "Fizz"
  if i%5 == 0:
    return "Buzz"
  return i

print(fizz_buzz(8))

#if you're using Return, you don't need to 
# use else or elif because the program is already 
# stopping after the return happens. If it's still going, 
# it'll just go to the next if,
# which is why you don't need "else: return i" because if 
# none of the ifs are met, it will return i
