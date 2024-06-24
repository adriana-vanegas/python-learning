#Functions with default values

# if you don't always want to add an argument, you can set up the parameter
# to equal a default value
# however, all parameters with default values should be added to 
# the end of the parameter list

def increment(number,by=1):
  return number + by


print(increment(number=5))