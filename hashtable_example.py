#!/bin/env/python3
# hashtable_example.py

# Demonstrate the hash table / dictionary data structure.
items1 = {"key1": "1", "key2": "2", "key3": "three"}
print(items1)

# TODO: Create a hash table / dictionary progressively.
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# TODO: Try to access a key that does not exist.
# print(items1["key4"])

# TODO: Replace an item in the hash table / dictionary.
items2["key1"] = "one"
print(items2)

# TODO: Iterate over the keys and values in a hash table / dictionary.
for key, value in items1.items():
    print("Key: ", key, " Value: ", value)
