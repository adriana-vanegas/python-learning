# Lambda Functions + Map and List Comprehensions

# Example 1: transform list into a list of prices
items_purchased = [('product_a',15),
                  ('product_b',10),
                  ('product_c',12)]

# Method 1 - 
price = []

for i in items_purchased:
  price.append(i[1])
print(price)

# Method 2 -
# Map function can iterate a list and apply a lambda function through each item on the list

price_values = list(map(lambda item:item[1], items_purchased))
print(price_values)

# Method 3 - Using List Comprehensions
# List expression syntax: [returned value for i in list]
list_prices = [val[1] for val in items_purchased]
print(list_prices)

# Example 2 - Map Function with Lambdas
list_numbers = list(range(1,21))

# Square each number
square = list(map(lambda num:num*num, list_numbers))
print(square)

squared = [val*2 for val in list_numbers]
print(squared)

# Example 3 - Capitalize all the words in the list
words = ['hello', 'world', 'python', 'lambda']

capital = []

# How I would do it normally
for i in words:
  capital_word = i.capitalize()
  capital.append(capital_word)
print(capital)

# How I would do it if I wanted to use map and lambda
capitals = list(map(lambda word:word.capitalize(), words))
print(capitals)

# Example 4 = Calculate Lengths:
words_2 = ['apple', 'banana', 'cherry', 'date']

length_2 = list(map(lambda word:len(word),words_2))
print(length_2)

length_2_lc = [len(word) for word in words_2]
print(length_2_lc)

# Example 5 - Find even or odd

numbers = [1, 2, 3, 4, 5]

# def even_or_odd(num):
#   for i in num:
#     if i % 2 == 0:
#       print(i,'Even')
#     else:
#       print(i,'Odd')

# even_or_odd(numbers)

even_odd = list(map(lambda val:'even' if val%2 == 0 else 'odd',numbers))
print(even_odd)

# List Comprehension Attempt
even_or_odd = ['even' if i%2 == 0 else 'odd' for i in numbers ]
# you can put if statements in the front of a list comprehension if you want it to be in the return value
print(even_or_odd)

# Example 6 - Add Corresponding Elements:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

corr = list(map(lambda val1,val2: val1+val2,list1,list2))

print(corr)

# addition = [val1 + val2 for val1, val2 in list1,list2]
# print(addition)
