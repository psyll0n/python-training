#!/usr/bin/env python3  

# Python Object Oriented Programming by Joe Marini.
# Basic class definition - Lesson 2. 

# TODO: Create a basic class.
class Book:
    # the __init__ function is called when an instance 
    # is created and ready to be initialized.
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: Add properties.
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
        
        
    # TODO: Create instance methods.
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount
                
        
# TODO: Create some instances of the class.
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "J.D. Salinger", 234, 29.95)


# TODO: Print the price of book1.
print(b1.getprice())



# TODO: Try setting the discount.
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())
        
        
# TODO: Properties with double underscores are hidden by the interpreter.
print(b2.__secret)



