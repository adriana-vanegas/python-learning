# Zip function
# Zip function can combine values from 2 or more lists

# Example 1
list1 = [1,2,3]
list2 = [10,20,30]

# goal: (1,10), (2,20), (3,30)
print(list(zip(list1,list2)))

print(list(zip("abc",list1,list2)))


#zip function in list comprehension
add = [val1+val2 for val1 ,val2 in zip(list1,list2)]
print(add)

# Example 2
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
hobby = ['Running','Tennis','Cars']
print(list(zip(names,ages,hobby)))

# Example 4 - Unzip a list of tuples into two separate lists
tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

print(list(zip(*tuples)))
# numbers = []
# letters = []

# for i in tuples:
#   val = i[0]
#   numbers.append(val)
#   let = i[1]
#   letters.append(let)
# print(numbers)
# print(letters)

# Calculate Averages
list_avg_1 = [10, 20, 30]
list_avg_2 = [40, 50, 60]


for x,y in zip(list_avg_1,list_avg_2):
  avg = (x+y)/2
  print(avg)

average = [(x+y)/2 for x,y in zip(list_avg_1,list_avg_2)]
print(average)