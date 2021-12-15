#!/usr/bin/env python3
# HTML Styling with decorators.

from functools import wraps


def bold(func):
    """Bold decorator"""

    @wraps(func)
    def wrapper():
        """Return html bold tags"""
        result = "<b>" + func() + "</b>"
        return result

    return wrapper


def italics(func):
    """Bold decorator"""

    @wraps(func)
    def wrapper():
        """Return html italics tags"""
        result = "<i>" + func() + "</i>"
        return result

    return wrapper


@bold
@italics
def printfib():
    """Return Fibonacci"""
    return "Fibonacci"


print(printfib())
