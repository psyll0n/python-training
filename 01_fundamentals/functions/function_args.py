#!/usr/bin/env python3
"""function_args.py - Demonstrates positional and keyword arguments.

This module shows the difference between:
- Positional arguments (required, order matters)
- Keyword arguments with default values (optional)
"""


def greeting(name, location):
    """Print a personalized greeting with location.
    
    Args:
        name (str): The person's name (required positional argument)
        location (str): The person's location (required positional argument)
    
    Note:
        Both arguments must be provided in the correct order.
    """
    print(f"Hello, {name}!")
    print(f"Your location is {location}")
    print(f"How are you doing today, {name}?")


# Call with positional arguments - order matters!
greeting("Alex", "Sofia")


def greeting_with_name(name="George", location="London"):
    """Print a greeting with default values for name and location.
    
    Args:
        name (str, optional): The person's name. Defaults to "George".
        location (str, optional): The person's location. Defaults to "London".
    
    Note:
        Arguments are optional due to default values.
        Can be called with no arguments, or override specific parameters.
    """
    print(f"Hello, {name}!")
    print(f"Your location is {location}")
    print(f"How are you doing today, {name}?")


# Call with default values (no arguments needed)
greeting_with_name()
