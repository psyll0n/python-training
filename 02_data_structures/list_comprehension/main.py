#!/usr/bin/env python3
"""list_comprehension_main.py - Comprehensive examples of list comprehensions.

This module demonstrates various list comprehension patterns:
- Basic transformations
- Filtering with conditionals
- Working with ranges
- String manipulations
- File processing
- Finding common elements

List comprehension syntax:
    [expression for item in iterable if condition]
    
Benefits:
- More concise than traditional loops
- Often faster execution
- More Pythonic and readable
"""

# Example 1: Simple transformation - add 1 to each number
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]  # Creates [2, 3, 4]
print(new_list)

# Example 2: Squaring numbers (mathematical transformation)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]  # Square each number
print(squared_numbers)

# Example 3: Using range() in list comprehension
range(1, 5)  # Creates sequence 1, 2, 3, 4
new_items_list = [num * 2 for num in range(1, 5)]  # Double each number
print(new_items_list)

# Example 4: Filtering with condition - names shorter than 5 characters
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)  # ['Alex', 'Beth', 'Dave']

# Example 5: Transformation + filtering - uppercase long names
capitalized_names = [name.upper() for name in names if len(name) > 5]
print(capitalized_names)  # ['CAROLINE', 'ELANOR', 'FREDDIE']

# Example 6: Type conversion + filtering - even numbers from strings
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
numbers = [int(i) for i in list_of_strings]  # Convert strings to integers
result = [i for i in numbers if i % 2 == 0]  # Filter even numbers only
print(result)

# Example 7: Finding common numbers between two files
# This demonstrates file I/O combined with list comprehensions

# Read the contents of file1.txt and file2.txt
with open("file1.txt") as file1:
    file1_numbers = file1.readlines()

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

# Convert the read lines into a list of integers
# strip() removes whitespace/newlines, int() converts to integer
file1_numbers = [int(num.strip()) for num in file1_numbers]
file2_numbers = [int(num.strip()) for num in file2_numbers]

# Use list comprehension to find common numbers (intersection)
result = [num for num in file1_numbers if num in file2_numbers]

# Print the result
print(result)
