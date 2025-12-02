#!/usr/bin/env python3
# item_counter.py - Using a hash table to count individual items.


# Define a set of items in which we want to count.
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

#  Create a hash table to perform the filter operation.
counter = dict()

#  Iterate over each item and increment the count for each one.
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1


#  Create a set from the resulting keys in the hash table.
print(counter)
