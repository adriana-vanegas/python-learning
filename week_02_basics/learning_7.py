#Nested Loops


#(x,y)
#(0,0)
#(0,1)
#(0,2)
#(1,0)
#(1,1)
#(1,2)

#x = [0,1]
#y = [0,1,2]

#for x_val in x:
#  for y_val in y:
#    print(f'({x_val},{y_val})')

# list = [2,2,2,2,5]

# for range_item in list:
#   output = ''
#   item = range_item
#   for row in range(item):
#     output += 'x'
#   print(output)


# 1,2,3,4
# 0,1,2,3

# for val in range(1,5):
#    output = ''
#    for reap in range(val):
#       output += str(val)
#    print(output)

laundry_basket = ['Shirt','Pants','Shorts','Socks']
closet = []

for i in laundry_basket:
   hanger = i + ' in hanger'
   closet.append(hanger)
print(closet)