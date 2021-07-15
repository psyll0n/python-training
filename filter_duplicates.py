#!/usr/bin/env python3
# filter_duplicates.py - remove duplicates by using a hash table.

# Define a set of items in which we want to remove duplicates.
items = [
    "apple",
    "orange",
    "apple",
    "pear",
    "orange",
    "banana",
    "orange",
    "apple",
    "pear",
    "banana",
    "mango",
    "kiwi",
    "plum",
    "banana",
    "pineapple",
    "strawberry",
    "cherry",
    "apple",
    "orange",
]

# TODO: Create a hash table to perform the filter operation.
filter = dict()

# TODO: Loop over the items and add them to the hash table.
for key in items:
    filter[key] = 0

# TODO: Create a set from the resulting keys in the hash table.
result = set(filter.keys())
print(result)
