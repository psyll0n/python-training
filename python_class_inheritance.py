#! /usr/bin/env python3

# Parent class
class Parent(object):
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('Parent.grok')
        self.spam()


# Use case #1
class Child1(Parent):
    def yow(self):
        print('Child1.yow')

# Use case #2
class Child2(Parent):
    def spam(self):
        print('Child.spam', self.value)        

# Use case #3
class Child3(Parent):
    def spam(self):
        print('Child3.spam')
        super().spam()      # Invokes the original spam() method.

# Use case #4     
class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)    # Initialize the parent.

# 2nd Parent class  
class Parent2(object):
    def yow(self):
        print('Parent2.yow')
        
# Child class that inherits from the Parent and Parent2 classes.
class Child5(Parent, Parent2):
    pass