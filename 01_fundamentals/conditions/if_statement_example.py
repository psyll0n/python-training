#!/usr/bin/env python3
"""if_statement_example.py - Demonstrates basic if statement usage in Python.

This module shows how to use if statements for conditional logic,
comparing numerical values using various comparison operators.

Comparison Operators:
    < : Less than
    > : Greater than
    <= : Less than or equal to
    >= : Greater than or equal to
    == : Equal to
"""

# Initialize variables for comparison
people = 20
cats = 30
dogs = 15

# Comparison using less than operator
if people < cats:
    print("Too many cats! The world is doomed!")

# Comparison using greater than operator
if people > cats:
    print("Not many cats! The world is saved!")

# Check if people count is less than dogs
if people < dogs:
    print("The world is drooled on!")

# Check if people count is greater than dogs
if people > dogs:
    print("The world is dry!")

# Increment dogs count by 5
dogs += 5

# Comparison using greater than or equal to operator
if people >= dogs:
    print("People are greater than or equal to dogs.")

# Comparison using less than or equal to operator
if people <= dogs:
    print("People are less than or equal to dogs.")

# Comparison using equality operator
if people == dogs:
    print("People are dogs.")
