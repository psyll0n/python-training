class Parent(object):
    def altered(self):
        print("PARENT altered()")


"""On the lines below, "super(Child, self).altered()" is used, which is aware of the inheritance and will get the Parent class.
this should be read as “call super with arguments Child and self, then call the function altered on whatever it returns.” """


class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
