#!/usr/bin/env python3
"""python_json_module.py - Demonstrates Python's json module for JSON handling.

The json module provides functions for encoding and decoding JSON:
- json.loads(): Parse JSON string -> Python object (deserialization)
- json.dumps(): Convert Python object -> JSON string (serialization)

JSON Data Type Mappings:
    Python -> JSON
    dict -> object
    list/tuple -> array
    str -> string
    int/float -> number
    True -> true
    False -> false
    None -> null

Common Parameters:
- indent: Pretty-print with indentation
- sort_keys: Sort dictionary keys alphabetically
"""

import json

# ===== Parsing JSON String (Deserialization) =====

# JSON string (note: uses double quotes)
x = '{ "name":"John", "age":30, "city":"New York"}'

# Parse JSON string into Python dictionary
y = json.loads(x)

# Access values from the resulting dictionary
print("Age from parsed JSON:", y["age"])  # Output: 30


# ===== Converting Python Object to JSON (Serialization) =====

# Python dictionary
x = {"name": "John", "age": 30, "city": "New York"}

# Convert Python dict to JSON string
y = json.dumps(x)

# The result is a JSON-formatted string
print("JSON string:", y)
# Output: {"name": "John", "age": 30, "city": "New York"}


# ===== Converting Various Python Types to JSON =====

print("\nConverting different Python types to JSON:")

# Dictionary -> JSON object
print("Dict:", json.dumps({"name": "John", "age": 30}))

# List -> JSON array
print("List:", json.dumps(["apple", "bananas"]))

# Tuple -> JSON array (tuples become arrays in JSON)
print("Tuple:", json.dumps(("apple", "bananas")))

# String -> JSON string
print("String:", json.dumps("hello"))

# Integer -> JSON number
print("Int:", json.dumps(42))

# Float -> JSON number
print("Float:", json.dumps(31.76))

# Boolean True -> JSON true
print("True:", json.dumps(True))

# Boolean False -> JSON false
print("False:", json.dumps(False))

# None -> JSON null
print("None:", json.dumps(None))


# ===== Complex Object with Pretty Printing =====

# Python object containing multiple data types
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),  # Tuple -> JSON array
    "pets": None,                   # None -> null
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ],
}

print("\nComplex object with formatting:")
# Pretty-print JSON with 4-space indentation and sorted keys
print(json.dumps(x, indent=4, sort_keys=True))
