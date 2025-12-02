#!/usr/bin/env python3
"""class_inheritance.py - Demonstrates the need for inheritance (before refactoring).

This module shows code duplication that can be solved with inheritance.
Notice how Book, Magazine, and Newspaper share common attributes (title, price)
but are defined as separate classes with duplicated code.

Problem:
- Code duplication (title, price appear in all three classes)
- Maintenance nightmare (changing one requires changing all)
- Violates DRY (Don't Repeat Yourself) principle

Solution:
- See class_hierarchy.py for inheritance-based refactoring
- Create a base Publication class with shared attributes
- Derive specific classes (Book, Magazine, Newspaper) from it

Credit: Based on Python Object Oriented Programming by Joe Marini
"""


class Book:
    """Represents a book publication.
    
    Attributes:
        title (str): Book title
        author (str): Book author
        pages (int): Number of pages
        price (float): Book price
    """
    
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages


class Magazine:
    """Represents a magazine publication.
    
    Attributes:
        title (str): Magazine title
        publisher (str): Publishing company
        price (float): Magazine price
        period (str): Publication frequency (e.g., "Weekly")
    
    Note:
        Shares 'title' and 'price' with Book - code duplication!
    """
    
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period


class Newspaper:
    """Represents a newspaper publication.
    
    Attributes:
        title (str): Newspaper name
        publisher (str): Publishing company
        price (float): Newspaper price
        period (str): Publication frequency (e.g., "Daily")
    
    Note:
        Nearly identical to Magazine - should share a base class!
    """
    
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.publisher = publisher
        self.period = period


# Create instances of each publication type
b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("The New York Times", "NY Times Company", 6.0, "Daily")
m1 = Magazine("The Time", "Time", 5.99, "Weekly")

# Access attributes - notice all have 'price' but it's duplicated in code
print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
