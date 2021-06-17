# Insert a function that prints a greeting, and execute it on the p1 object:
# Objects can also contain methods. Methods in objects are functions that belong to the object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables
# that belong to the class.
# It does not have to be named self, it can be called with whatever name we like, but it has to be the first parameter
# of any function in the class.


# Use the words mysillyobject and abc instead of self:


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
