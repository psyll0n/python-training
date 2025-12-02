#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Python Data Classes. Available in version 3.7 and above.
# Creating immutable data classes.

from dataclasses import dataclass


# The "frozen" parameter makes the class immutable.
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def someFunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)


# Attempting to change the value of an immutable class will throws an exeption.
# obj.value1 = "New Value"
# print(obj.value1)

# Even functions within the class cannot change anything.
obj.someFunc(20)
