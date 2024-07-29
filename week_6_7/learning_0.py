#Exceptions
import logging

list_val = [10,2,4,0,5,'a']

for val in list_val:
  try:
      print(10/int(val))
  except (ZeroDivisionError, ValueError) as e:  # Always be explicit about the type of error as a best practice
    print("Error detected. Division failed.")
    print(e)
    continue  # or you can use pass to skip it
  except Exception as e:
     logging.exception(e) #If any other errors occur that you don't expect, then you can log/track the exceptions
     # This is a best practice to improve your code in the future


# Raise an exception
# Raising an exception means that you will let the 
# error crash (i.e. full error statement will be raised and program will crash)

# Finally
# Regardless of whether or not there is an exception, finally will execute an action

try:
   value = int('hello')
except ValueError:
   print('Program crashed!')
   raise
finally:
   print("This will be printed regardless if there is or isn't an exception")


# Else 
# If there is no Exception, then "else" can execute an action

set_of_values = ['hello',5]
for num in set_of_values:
  try:
    print(int(num))
  except ValueError:
    print("This will run if there is an error")
  else: 
     print("This will run if there's no error")
  finally:
    print("This will be printed regardless if there is or isn't an exception")