#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Magic Methods - Equality and Comparison magic methods.


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: The __eq__ method is called when we compare two objects.
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare Book to a non-Book.")
        return (
            self.title == value.title
            and self.author == value.author
            and self.price == value.price
        )

    # TODO: The __lt__ method establishes < relationship with another object.
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare Book to a non-Book.")

        return self.price >= value.price

    # TODO: The __gt__ method establishes >= relationship with another object.
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Cannot compare Book to a non-Book.")

        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "J.D. Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("How to Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality.
print(b1 == b3)
print(b1 == b2)


# TODO: Check for greater and lesser value.
print(b2 >= b2)
print(b2 < b1)

# TODO: Now we can sort our books too.
books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])
