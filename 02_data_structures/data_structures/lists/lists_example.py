#!/usr/bin/env python3
"""lists_example.py - Demonstrates common list operations in Python.

This module shows:
- String splitting to create lists
- List manipulation with pop() and append()
- List indexing and slicing
- Joining list elements into strings

Key list methods used:
- split(): Convert string to list
- pop(): Remove and return last item
- append(): Add item to end of list
- join(): Combine list items into string
"""

# Start with a string of items (not actually 10 things!)
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Split string into list using space as delimiter
stuff = ten_things.split(" ")

# Additional items to add to our list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# Keep adding items until we have exactly 10
while len(stuff) != 10:
    next_one = more_stuff.pop()  # Remove last item from more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one)  # Add item to end of stuff
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

# Indexing: Access element at position 1 (second item)
print(stuff[1])

# Negative indexing: Access last element
print(stuff[-1])

# pop(): Remove and return last element
print(stuff.pop())

# join(): Combine all elements into a single string
print("".join(stuff))

# join() with slicing: Join elements from index 3 to 4 with '#' separator
print("#".join(stuff[3:5]))
