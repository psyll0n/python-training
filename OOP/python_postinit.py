#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Python Data Classes. Available in version 3.7 and above.
# The __post_init__ function.

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: The __post_init__ function allows us to customize
    # additional properties after the object has been created.
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# Create some instances of the Book class.
b1 = Book("The C Programming Language", "Brian W. Kernighan", 300, 32.50)
b2 = Book("The Unix Programming Environment", "Brian W. Kernighan", 38, 29.50)
b3 = Book("The C Programming Language", "Brian W. Kernighan", 300, 32.50)


# TODO: Use the description attribute to print the title of each book.
print(b1.description)
print(b2.description)
print(b3.description)
