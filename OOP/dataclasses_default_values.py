#!/usr/bin/env python3
# Python Object Oriented Programming by Joe Marini.
# Python Data Classes. Available in version 3.7 and above.
# Implementing default values in data classes.

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)



    
b1 = Book("The C Programming Language", "Brian W. Kernighan", 300)
b2 = Book("The Unix Programming Environment", "Brian W. Kernighan", 380)
print(b1)
print(b2)
    