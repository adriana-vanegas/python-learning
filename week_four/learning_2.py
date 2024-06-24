#2D lists

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

line= 0

for row in matrix:
  line = 0
  for i in row:
    line += i
  print(line)