#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Python Magic calls.


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # The __call__ method is used to call the object like a function.
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("The Sun", "John Smith", 20.0)
b2 = Book("The Moon", "John Smooth", 30.0)


# Call the object as if it were a function.
print(b1)
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
