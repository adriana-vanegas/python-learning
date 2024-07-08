# Arrays
# Arrays are better than lists at holding memory when you have
# a large list of numbers, like 10k +

# For 90% of cases, you will use lists unless you see performance issues 
# (don't try to optimize unless you have a problem)

from array import array

numbers = array('i',[1,2,3])
# For arrays, you need to use the right typecode: https://docs.python.org/3/library/array.html
# i typecode is for integers, so you can't append non-integers
numbers.append('a')

print(type(numbers))
print(numbers)