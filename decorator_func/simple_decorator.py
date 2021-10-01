#!/usr/bin/env python3

# A decorator is a callable that takes another function as an argument,
# extending the behaviour of that function without explicitly modifying
# that function.


# Decorator template
# def my_decorator(func):
#    '''Decorator function'''
#   def wrapper():
#       # Do something before
#       result = func()
#       # Do something after
#       return result
#   return wrapper
#
#
# @my_decorator
# def my_func()
#   pass


def my_decorator(func):
    """Decorator function"""

    def wrapper():
        """Wrapper function. Return
        strin F-I-B-O-N-A-C-C-I"""
        return "F-I-B-O-N-A-C-C-I"

    return wrapper


@my_decorator
def pfib():
    """Return Fibonacci"""
    return "Fibonacci"


print(pfib())
