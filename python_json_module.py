# Import the Python JSON module. Parse it and the print out a specific velue from the dictionary.

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {"name": "John", "age": 30, "city": "New York"}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Convert a Python object containing all the legal data types:

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

print(json.dumps(x, indent=4, sort_keys=True))
