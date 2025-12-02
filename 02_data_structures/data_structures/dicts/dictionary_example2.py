#!/usr/bin/env python3
"""dictionary_example2.py - Demonstrates basic dictionary operations.

This module shows:
- Creating an empty dictionary
- Adding key-value pairs
- Accessing dictionary values by key
- Taking user input for dictionary data

Dictionaries store data as key-value pairs, providing fast lookups.
"""

# Create an empty dictionary (alternative: phonebook = dict())
phonebook = {}

# Get user input for name (dictionary key)
name = input("Enter name: ")

# Get user input for phone number (dictionary value)
number = int(input("Enter phone number: "))

# Add the name-number pair to the dictionary
phonebook[name] = number

# Display the entire phonebook dictionary
print(phonebook)

# Access a specific entry by key (assumes "Alex" was entered)
# Note: This will raise KeyError if "Alex" is not in the dictionary
print(phonebook["Alex"])
