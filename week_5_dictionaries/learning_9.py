# Tuples
# Read only list, cannot be modified or changed
# can be used with or without ()
# For example geographic coordinates shouldn't change

point = (1,2)

point_1 = 1,2 # still a tuple
point_2 = 1, # a tuple with one number
point_3 = 1 # NOT a tuple, it's a variable

tuples = (1,2)*3
print(tuples)

# Can convert lists to tuples

convert = tuple([1,2,3])
print(convert)