# Dunder methods, also known as magic methods, are special methods in Python that have double 
# underscores at the beginning and end of their names. They allow us to define how our objects
# behave with built-in functions and operators. In this example, we will create a Book class that
# uses dunder methods to provide a string representation of the book and to calculate the number of 
# words in the book's content.
class Book:
    """A class that represents a book with a title, number of pages, and content.
    
    Attributes:
        title (str): The title of the book.
        pages (int): The number of pages in the book.
        content (str): The content of the book.
    """
    # In Python the __init__ is called a dunder method.
    def __init__(self, title, pages, content):
        self.title = title
        self.pages = int(pages)
        self.content = content

    # The __str__ method is a dunder method that returns a string representation of the object.
    # In this case, we will return the title of the book when we print the object.
    def __str__(self):
        return self.title
    
    # The __len__ method is a dunder method that returns the length of the object.
    # In this case, we will return the number of words in the content of the book.
    def __len__(self):
        words = self.content.split(" ")
        return len(words)


harry_potter = Book(
    "Harry Potter", 250, "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
)
print(type(harry_potter))
print(len(harry_potter))


lotr = Book(
    "Lord of the Rings", 900, "Lorem ipsum dolor sit amet, consectetur adipiscing..."
)
print(type(lotr))
print(len(lotr))
