#!/usr/bin/env python3
# Preserving docstring metadata in decorator functions.

from functools import wraps


def make_posh(func):
    """This is the function decorator."""

    @wraps(func)
    def wrapper():
        """This is the wrapper function."""
        print("+-------+")
        print("|       |")
        result = func()
        print(result)
        print("|       |")
        print("+-------+")
        return result

    # In order to preserve the docstring metadata we use the following.
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    # The same is possible with 'wraps' which is available in 'functools'.
    return wrapper


@make_posh
def printfib():
    """Print the Fibonacci sequence."""
    return "Fibonacci"


printfib()
