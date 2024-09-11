#!/usr/bin/env python3
# queue_example.py

# Try out Python Queue functions.
from collections import deque

#  Create a new empty deque object.
queue = deque()

#  Add some items to the queue.
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#  Print the queue contents.
print(queue)

#  Remove an item from the queue.
x = queue.popleft()
print(x)
print(queue)
