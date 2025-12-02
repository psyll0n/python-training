#!/usr/bin/env python3
"""if_elif_else_statement.py - Demonstrates if-elif-else conditional statements.

This module shows how to use if-elif-else chains to handle multiple
conditional branches and provide a default case when no conditions are met.

The else clause executes when none of the if/elif conditions are True.
"""

# Initialize transportation variables
people = 30
cars = 40
trucks = 15

# Decision making: Should we take the cars?
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    # This executes when cars == people
    print("We can't decide.")

# Decision making: What about the trucks?
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    # This executes when trucks == cars
    print("We still can't decide.")

# Final decision: Compare people and trucks
if people > trucks:
    print("Alright, let's take the trucks.")
else:
    # This executes when people <= trucks
    print("Fine, let's stay home then.")
