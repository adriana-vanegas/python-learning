# Dictionary

# The dictionary can store lists in values
student = {'name':'John', 'age':25, 'courses': ['Math','History']}

# To print values that are not available
print(student['age'])
print(student.get('phone','not found'))

# To add phone
student['phone']= '555-5555'
print(student)

# Update values
student['name']= 'Adriana'
# or
student.update({'age':26, 'phone':'565-5555'})
print(student)

# To delete student age
del student['age']
# or
phone_num = student.pop('phone')
print(student)
print(phone_num)

print(len(student))

# To see only the elements of the dictionary
print(student.keys()) # only the keys
print(student.values()) # only the values
print(student.items()) # all items in the dictionary

# Loop through dictionary
for key in student:
  print(key)

for value in student.values():
  print(value)

for key,value in student.items():
  print(key, value)