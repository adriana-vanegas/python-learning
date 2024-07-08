# Lambda + Filter and List Comprehensions

# Example 1
items_purchased = [('product_a',15),
                  ('product_b',10),
                  ('product_c',12)]

greater_than_10 = list(filter(lambda val:val[1] > 10, items_purchased))
print(greater_than_10)


# Example 2 Extract even values
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda val:val%2==0,numbers))
print(even)

# Using List expressions
# List expression syntax: [returned value for i in list if statement]

even2 = [val for val in numbers if val%2==0]
#this is saying return the value in the numbers list if it's even
print(even2)


#Example 3 - Filter Strings Containing 'a':

words = ['apple', 'banana', 'cherry', 'date']

lamb_contain_a = list(filter(lambda has_a:'a' in has_a,words))
print(lamb_contain_a)

contain_a = [has_a for has_a in words if 'a' in has_a]
# this is saying return the word in the list of words that has 'a'
print(contain_a)



# Example 4 - find positive value
numbers_1 = [-1, 2, -3, 4, -5]

positive = [val for val in numbers_1 if val > 0]
print(positive)

lamb_positive = list(filter(lambda val:val>0, numbers_1))
print(lamb_positive)