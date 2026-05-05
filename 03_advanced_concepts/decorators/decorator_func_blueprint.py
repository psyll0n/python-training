#!/usr/bin/env python3
# Decorator function blueprint.

from functools import wraps

# Note: @wraps takes a function to be decorated and adds the functionality of copying
# over the function name, docstring, arguments list, etc. This allows us to access the
# pre-decorated function’s properties in the decorator.


def decorator_name(f):
    """A simple decorator function that demonstrates the use of @wraps.
    
    This decorator checks a global variable `can_run` to determine if the decorated function should execute.
    If `can_run` is False, it returns a message instead of calling the function.
    If `can_run` is True, it calls the decorated function as normal.
    
    Args:
        f (callable): The function to be decorated
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    """ A simple function that prints a message. This function is decorated with `decorator_name`."""
    print("Function is running.")


can_run = True
print(func())


can_run = False
print(func())

print("\n" + "="*70)
print("STANDARD DECORATOR BLUEPRINT")
print("="*70)
