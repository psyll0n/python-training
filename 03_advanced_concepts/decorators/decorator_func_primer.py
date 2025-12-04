#!/usr/bin/env python3

"""
Python Decorator Function Primer
--------------------------------
This script demonstrates how to use decorators in Python to wrap functions and modify their behavior.
It covers:
    - Basic decorator implementation
    - The @decorator syntax
    - The importance of preserving function metadata using functools.wraps
"""


# Basic Decorator Function
def basic_decorator(func):
    """
    A decorator function that wraps another function to add behavior before and after its execution.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with added behavior.
    """
    def wrapper():
        print("[Decorator] Doing some work before executing the function...")
        func()
        print("[Decorator] Doing some work after executing the function...")
    return wrapper


def undecorated_function():
    """
    Example function that will be decorated to enhance its functionality.
    """
    print("I am the function which needs some decoration to remove my foul smell.")

# --- Manual decoration (long way) ---
print("Manual decoration (long way):")
undecorated_function()
undecorated_function = basic_decorator(undecorated_function)
undecorated_function()

# --- Using @decorator syntax (short way) ---
print("\nShort way of defining a decorator function:")

@basic_decorator
def decorated_function():
    """
    Another example function to demonstrate decorator usage.
    """
    print("I am the function which needs some decoration to remove my foul smell.")

decorated_function()

# Demonstrate the issue with function metadata
print(f"Function name after decoration: {decorated_function.__name__}")
# Output: wrapper

# --- Solution: Use functools.wraps to preserve metadata ---
print("\nUsing functools.wraps to preserve function metadata:")
from functools import wraps

def metadata_preserving_decorator(func):
    """
    A decorator function that wraps another function to add behavior before and after its execution.
    Uses functools.wraps to preserve the original function's metadata.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with added behavior and preserved metadata.
    """
    @wraps(func)
    def wrapper():
        print("[Decorator] Doing some work before executing the function...")
        func()
        print("[Decorator] Doing some work after executing the function...")
    return wrapper

@metadata_preserving_decorator
def function_with_metadata():
    """
    Hey yo! Decorate me!
    """
    print("I am the function which needs some decoration to remove my foul smell.")

print(f"Function name after decoration: {function_with_metadata.__name__}")
