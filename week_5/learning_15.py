# Generator Expressions
# Generator Objects are iterable but they don't store values in memory,
# they just generate a new value with each iteration

from sys import getsizeof

generator_obj = (x * 2 for x in range(10000000))
print(len(generator_obj))
print("gen:", getsizeof(generator_obj))


list = [x * 2 for x in range(10000000)]

print("gen:", getsizeof(list))

# Whenever you deal with an infinite stream of data or a really large data set
# use a generator object. The only downside is that it 


# for x in values:
#   print(x)

