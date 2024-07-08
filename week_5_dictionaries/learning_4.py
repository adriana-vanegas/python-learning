# Lambda functions

# Lambda functions are tiny "anonymous" (don't have a defined name) functions 
# that you just want to write once

#Within a lambda function, you can write the arguments of the function and what value you want to return


# Example 1:
subtract = lambda x,y: x- y 

print(subtract(5,3))


# Example 2:
grade_list = [['Johnny',3.5,18],['Mel',3.9,17],['Pedro',3.8,19]]

grade_list.sort(key = lambda student:student[1],reverse = True)

print(grade_list)


# Example 3: transform list into a list of prices
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


# Example 4 - Map Function with Lambdas
list_numbers = list(range(1,21))

# Find which numbers can be squared
square = list(map(lambda num:num*num, list_numbers))
print(square)