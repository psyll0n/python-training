# In Python the __init__ is called a dunder method.
class Book:
    def __init__(self, title, pages, content):
        self.title = title
        self.pages = int(pages)
        self.content = content

    def __str__(self):
        return self.title

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
