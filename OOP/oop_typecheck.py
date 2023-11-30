#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini.
# Checking class types and instances.


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes.
b1 = Book("The Cather in the Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")


# TODO: Use type() to inspect the object types.
print(type(b1))
print(type(b2))
print(type(n1))
print(type(n2))

# TODO: Compare the types of the objects.
print(type(b1) == type(b2))
print(type(b1) == type(n1))


# TODO: Use isinstance() to compare a specific instance to a known type.
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))
