# Lists: Adding, removing, finding items, and sorting

letters = ['a','b','c','d']

###################
#       ADD       #
###################


# Add at the end of the list
letters.append('e')
print(letters)

# Add in a specific index
letters.insert(1,'!')
print(letters)


###################
#      REMOVE     #
###################

# Remove the end of the list
letters.pop()
print(letters)

# Remove a specific index
letters.pop(1)
print(letters)

#Remove first value if you don't know the index
letters.remove('b')
print(letters)

# Remove a range of items (not just one)
del letters[1:]
print(letters)

# Clear
# letters.clear()
# print(letters)

###################
#      FIND       #
###################

letters_2 = ['a','b','c','d']

# To find an item
print(letters_2.index('b'))

# If you want to check if an item is in a list
print(letters_2.count('e'))

for i in letters_2:
  if 'e' in i:
    print(i)


###################
#     SORTING     #
###################

numbers = [1,40,29,16]
letters_check = ['c','g','a','p']

# Sort works with numbers and letters
numbers.sort()
letters_check.sort()

print(sorted(numbers)) #sorted creates a new list that doesn't modify the original list
print(numbers)
print(letters_check)

# Sort works with numbers and letters
numbers.reverse()
letters_check.reverse()

print(sorted(numbers,reverse=True)) #sorted creates a new list that doesn't modify the original
print(numbers)
print(letters_check)


# Sort complex lists, like Matrices
# For example, let's order these products by their price
items_purchased = [('product_a',15),
                  ('product_b',10),
                  ('product_c',12)]


# To do that we can use the sort function and use key
# The key expects a function to be applied on each element of the list - The function 
# should return a value by which you want to order by

# # The sort item function specifies to return index 1 for each tuple in the matrix
# def sort_item(item):
#   return item[1]

# We can pass this function to the sort key - where it will iterate over each item in the matrix
# i.e. the function doesn't need a loop, because the sort automatically loops over the tuples
# items_purchased.sort(key = sort_item)

# Lambda functions are tiny "anonymous" (don't have a defined name) functions 
# that you just want to write once

#Within a lambda function, you can write the arguments of the function and what value you want to return

items_purchased.sort(key = lambda item:item[1])

print(items_purchased)