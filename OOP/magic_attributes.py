#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# The __getattr__, __getattribute__, and __setattr__ methods.


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ method is used to return a user-friendly string
    # representation of the object.
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name, otherwise a recursive loop is created.
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # TODO: __setattr__ called when an attr value is set. Don't set the value
    # directly, here, otherwise a recursive loop causes a crash.
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) != float:
                raise ValueError("Price must be a float")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method.
    def __getattr__(self, name):
        return f"{name} not found!"


b1 = Book("The C Programming Language", "Brian W. Kernighan", 35.95)
b2 = Book("The Unix Programming Environment", "Dennis Ritchie", 49.95)

b1.price = 35.95
print(b1)

b2.price = 40.0
print(b2)

print(b1.randomprop)
