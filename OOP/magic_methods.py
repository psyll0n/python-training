#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Magic Methods - String representation.
# Using the __str__ and __repr__ magic methods.


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        
    # TODO: Use the __str__ method to return a string.
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}" 
    
    # TODO: Use the __repr__ method to return an object representation.
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"
    
b1 = Book('War and Peace', 'Leo Tolstoy', 39.95)
b2 = Book('The Catcher in the Rye', 'J.D. Salinger', 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))


