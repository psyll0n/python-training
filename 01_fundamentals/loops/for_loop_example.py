#!/usr/bin/env python3
"""for_loop_example.py - Demonstrates for loop control flow with continue and break.

This module shows:
- Iterating over tuples with for loops
- Using 'continue' to skip the current iteration
- Using 'break' to exit the loop early
- List comprehension as shorthand syntax for loops
"""

# Define a tuple with colours
colours = ("Orange", "Green", "Yellow", "Blue", "Red", "Purple")

# Loop through the colours in the tuple, use 'continue' to skip an item
print("Starting the loop...")
for colour in colours:
    if colour == "Orange":
        continue  # Skip "Orange" and move to next iteration
    print(colour)
print("Loop has ended.")


# Define a second tuple with colours
colours2 = ("Orange", "Green", "Yellow", "Blue", "Red", "Purple")

# Loop through the colours. 'break' terminates the loop when condition is met
print("Starting the loop...")
for colour in colours2:
    if colour == "Blue":
        break  # Exit loop immediately when "Blue" is encountered
    print(colour)
print("Loop has ended.")


# List comprehension: for loop shorthand syntax
# This is a more Pythonic way to iterate and perform operations
print("for loop shorthand")
[print(x) for x in colours]
