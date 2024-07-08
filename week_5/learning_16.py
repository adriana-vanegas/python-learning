# Unpacking operator

numbers = [1,2,3]
# To get the values in this format : 1 2 3 (no [] or commas)
print(*numbers)
print(numbers)



list_created = list(range(5))
print(*list_created)

# You can unpack strings as well
print(*'Hello')
print(*range(5))


first = [1,2]
second = [3]
combine = first + second
print(*combine)


# To Unpack Dictionaries

one = {'x':1}
two = dict(x=10,y=2)
combo = {**one, **two,'z':1}
print(combo)
