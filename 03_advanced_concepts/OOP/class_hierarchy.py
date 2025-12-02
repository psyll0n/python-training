#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini.
# Understanding Class inheritance and hierarchy.


# Parent / base class
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# Parent / base class two that inherits from the Publication base class.
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


# Child / derived class inherits from the Publication parent class.
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


# Child / derived class inherits from the Periodical parent class.
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


# Child / derived class inherits from the Periodical parent class.
class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


b1 = Book("The C Programming Language", "Brian W. Kernighan", 228, 20.0)
n1 = Newspaper("The NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("The Python Journal", "Python Software Foundation", 12.0, "Quarterly")

print(b1.title)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
