#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini.
# Using class-level and static methods to create a class.


class Book:
    # TODO: Properties defined at the class level are shared by all instances of the class.
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: Double underscore properties are hidden from other classes.
    __booklist = None

    # TODO: Create a class method.
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: Create a static method.
    @staticmethod
    def getBooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # Instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance.
    def setTitle(self, newTitle):
        self.title = newTitle

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute.
print("Book types: ", Book.getBookTypes())

# TODO: Create some book instances.
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "EBOOK")

# TODO: Use the static method to access a singleton object.
theBooks = Book.getBooklist()
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)
