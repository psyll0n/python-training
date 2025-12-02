#!/usr/bin/env python3
"""args_and_kwargs_example.py - Demonstrates *args and **kwargs in Python.

This module explains:
- *args: Arbitrary positional arguments (stored as tuple)
- **kwargs: Arbitrary keyword arguments (stored as dictionary)
- How to use them together in function signatures

Function signature pattern:
    def func_name(name, *args, **kwargs)
    
Parameter order must be:
    1. Regular positional arguments
    2. *args
    3. **kwargs
"""


def func_name(*args):
    """Accept any number of positional arguments.
    
    Args:
        *args: Variable length argument list
    
    Note:
        args is a tuple containing all positional arguments
    """
    print(args)
    print(type(args))  # Will print: <class 'tuple'>


# Call with multiple arguments of different types
func_name(1, 5, 8, "Python", "Coding")


def print_args(*args):
    """Print each argument on a separate line.
    
    Args:
        *args: Variable length argument list
    """
    for arg in args:
        print(arg)


print("Computer", "Coffee", "Cup", "Monitor", "Lamp")


def my_func(**kwargs):
    """Accept any number of keyword arguments.
    
    Args:
        **kwargs: Arbitrary keyword arguments
    
    Note:
        kwargs is a dictionary with argument names as keys
    """
    print(kwargs)
    print(type(kwargs))  # Will print: <class 'dict'>


# Call with keyword arguments - creates a dictionary
my_func(name="Kalob", drink="Cofee", hobby="Gardening")


def my_second_func(**kwargs):
    """Iterate through keyword arguments and print key-value pairs.
    
    Args:
        **kwargs: Arbitrary keyword arguments
    """
    for key, value in kwargs.items():
        print("Key: ", key, " \t\t", "Value: ", value)


my_second_func(name="Kalob", drink="Cofee", hobby="Gardening")

def order(name, *dishes, **kwargs):
    """Process a food order with name, dishes, and optional delivery info.
    
    Args:
        name (str): Customer name (required positional argument)
        *dishes: Variable number of dish names
        **kwargs: Additional options (e.g., address for delivery)
    
    Example:
        order("John", "Pizza", "Pasta", address="123 Main St")
    """
    print(f"Hello {name}")
    
    # Iterate through all ordered dishes
    for dish in dishes:
        print(f"\tYou ordered {dish}")
    
    # Check if delivery address was provided
    if kwargs.get("address"):
        address = kwargs.get("address")
        print(f"We are delivering to {address}")
    else:
        print("You did not provide an address!")


order("Zephyr", "tacos", "cat food")
