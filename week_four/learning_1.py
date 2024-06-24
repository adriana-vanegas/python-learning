#Finding max value in list

list = [13,6,2,12,1]
max_value = list[0]

for i in list:
  if max_value < i:
    max_value = i
print(max_value)


#Check if number is even
number = range(1,10)
total = 0

for val in number:
  if val%2 == 0:
    total += 1
    print(val)
print(total)
