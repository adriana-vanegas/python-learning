def add(list):
  value = [2,4,5]
  for i in value:
    list.append(i)

def remove(list):
  list.pop(0)


def starting():
  list = []
  add(list)
  print(list)
  remove(list)
  print(list)

starting()