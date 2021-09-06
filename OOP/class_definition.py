#!/usr/bin/env python3

# Python Object Oriented Programming by Joe Marini.
# Basic class definition - Lesson 1.

# TODO: Create a basic class.
class Book:
    # the __init__ function is called when an instance 
    # is created and ready to be initialized.
    def __init__(self, title):
        self.title = title
        
        
# TODO: Create instances of the class.
b1 = Book("The Grapes of Wrath")
b2 = Book("The Great Gatsby")
b3 = Book("Brave New World")
b4 = Book("War and Peace")
        
        
# TODO: Print the class and property.
print(b1)
print(b1.title)


