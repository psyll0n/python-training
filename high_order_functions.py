#!/usr/bin/env python3
# high_order_functions.py - Demonstrates the concept of function hierarchy in Python 3.

import time


# High order function.
def add(x, y):
    # Low order function.
    def do_add():
        print("Adding {} + {} ->".format(x, y, x+y))
        return x+y
    return do_add


a = add(2,3)

print(type(a))

a()

b = add('hello', 'world')

b()

def after(seconds, func):
    time.sleep(seconds)
    func()

def hello():
    print('Hello, World!')    
    

after(5, hello)

after(3, add(5, 10))


