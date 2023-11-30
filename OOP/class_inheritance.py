#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini.
# Understanding Class inheritance.
# The code here can be refactored as demonstrated in class_hierarchy.py


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period


b1 = Book("Brave New Wordl", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("The New York Times", "NY Times Company", 6.0, "Daily")
m1 = Magazine("The Time", "Time", 5.99, "Weekly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
