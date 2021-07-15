#!/usr/bin/env python3
# queue_example.py

# Try out Python Queue functions. 
from collections import deque

# TODO: Create a new empty deque object.
queue = deque()

# TODO: Add some items to the queue.
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: Print the queue contents.
print(queue)

# TODO: Remove an item from the queue.
x = queue.popleft()
print(x)
print(queue)

