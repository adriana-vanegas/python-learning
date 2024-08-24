#Swapping Variables

x = 10
y = 11

z = x  # z = 10

x = y # x = 11
y = z # y = 10
print('x',x)
print('y',y)

# Or you can make y and x into a tuple (which doesn't change!)

x,y = y, x # this is a tuple even if it doesn't have ()
# or
x, y = (y, x)

print('x',x)
print('y',y)