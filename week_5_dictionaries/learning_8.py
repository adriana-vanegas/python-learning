# Stack
# Last in, first out data structure

browse = []

browse.append(1)
browse.append(2)
browse.append(3)

print(browse)

last = browse.pop()

print(last)
print(browse)
print('redirect',browse[-1])
if not browse: #if not browse means that the list is empty
  print('disable')


#Queue 
#First in, first out
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.appendleft(0)
print(queue) 
queue.popleft()
print(queue)