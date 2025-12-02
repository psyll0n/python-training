# Class definition example in Python


class MyClass:
    course = "Python for Everybody."

    def __init__(self, param1):
        # self.param1 here is similar to "param1 = 'Default value'

        self.param1 = param1
        print(param1)


new_class = MyClass("The first param")

type(new_class)
print(type("str"))
