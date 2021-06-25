
#! python3 
# collections: Counter, namedtuple, OrderedDictionary, defaultdict, dequeue

from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()
print(d)

d.extendleft([4, 5, 6])
print(d)

d.rotate(1)
print(d)
