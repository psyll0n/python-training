#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Understanding multiple inheritance.

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"
        

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar" 
        self.name = "Class B"
        

class C(A, B):
    def __init__(self):
        super().__init__()
        
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
        

c = C()
c.showprops()
print(C.__mro__)
