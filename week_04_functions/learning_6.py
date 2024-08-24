#Functions with double asterisk --> can pass multiple 
# keyword arguments to a function and return a dictionary

def save_user(**user):
  print(user["id"])

save_user(id=1, name="Adri", age = 15)

#Local variables: variables that are in the function and not anywhere else
#Global variable: variable that's outside of a function and 
# available anywhere in the file