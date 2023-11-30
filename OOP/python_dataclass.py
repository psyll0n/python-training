#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Python Data Classes. Works in version 3.7 and above.

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookInfo(self):
        return f"{self.title} by {self.author}, costs {self.price}"


# Create some instances of the Book class.
b1 = Book("The C Programming Language", "Brian W. Kernighan", 300, 32.50)
b2 = Book("The Unix Programming Environment", "Brian W. Kernighan", 38, 29.50)
b3 = Book("The C Programming Language", "Brian W. Kernighan", 300, 32.50)

# Access fields of the class.
print(b1.title)
print(b2.author)

# TODO: Print the book itself - dataclasses implement __repr__.
print(b1)

# TODO: Comparing two dataclasses - they automatically implement __eq__.
print(b1 == b3)

# TODO: Change some fields of the class.
b1.title = "Anna Karenina"
b1.author = "Leo Tolstoy"
b1.pages = 864
b1.price = 49.99
print(b1.bookInfo())
