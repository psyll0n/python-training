#!/usr/bin/env python3

# Python Decorator function example.
# Decorators wrap a function and modify its behaviour in one way or another. 


def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
    
a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()


# With the @a_new_decorator we can use the short way of defining the same decorator function.
print("Short way of defining a decorator function.")


@a_new_decorator
def a_function_requiring_decoration():
    """Hey, you decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")
    
a_function_requiring_decoration()



print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction

# The output is not what we expected! Its name is “a_function_requiring_decoration”. Well,
# our function was replaced by wrapTheFunction. It overrode the name and docstring
# of our function. Luckily, Python provides us a simple function to solve this problem
# and that is functools.wraps.

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
    "remove my foul smell")


print(a_function_requiring_decoration.__name__)