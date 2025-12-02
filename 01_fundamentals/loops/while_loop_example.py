#!/usr/bin/env python3
"""while_loop_example.py - Demonstrates while loop iteration over a list.

This module shows how to use a while loop to iterate through list elements
using an index counter. While loops continue executing as long as the
condition remains True.

Note: For list iteration, a for loop is typically more Pythonic,
but this example demonstrates while loop mechanics.
"""

# Define a list of fruits
thisisalist = ["banana", "mango", "kiwi", "orange", "melon", "apricot", "peach"]
print(thisisalist)

# Initialize counter variable for iteration
i = 0

# While loop: iterate as long as i is less than list length
while i < len(thisisalist):
    print(thisisalist[i])  # Print current fruit
    i = i + 1  # Increment counter (prevents infinite loop)
