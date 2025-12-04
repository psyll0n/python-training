#!/usr/bin/env python3
# Decorator function blueprint.

from functools import wraps

# Note: @wraps takes a function to be decorated and adds the functionality of copying
# over the function name, docstring, arguments list, etc. This allows us to access the
# pre-decorated function’s properties in the decorator.


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    """Function Docstring"""
    print("Function is running.")


can_run = True
print(func())


can_run = False
print(func())

print("\n" + "="*70)
print("STANDARD DECORATOR BLUEPRINT")
print("="*70)
