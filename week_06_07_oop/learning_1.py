# Cost of Raising Exceptions
# It take 45x longer to run a code that raises an exception
# See if a simple if statement can help


from timeit import timeit # To calculate execution time of python code

code1 ="""
def age_generator(age):
  if age <= 0:
    raise ValueError("Age cannot be less than 0")
  return 10 / age

try:
  age_generator(-1)
except ValueError as error:
  print(error)
"""

code2 ="""
def age_generator(age):
  if age <= 0:
    return None
  return 10 / age

output = age_generator(-1)

if output == None:
  pass
"""


print("code1",timeit(code1,number=100000)) # number of times to execute the code1
print("code2",timeit(code2,number=100000)) 
