#!/usr/bin/env python3
"""simple_decorator.py - Introduction to basic decorator patterns.

This module demonstrates:
- The fundamental concept of decorators
- Basic decorator template structure
- How decorators wrap and modify function behavior
- The @ symbol as syntactic sugar for decorator application

A decorator is a callable (usually a function) that takes another function
or class as an argument, and returns a modified version of that function or
class. Decorators provide a clean, readable way to extend or modify the
behavior of functions and classes without permanently changing their source code.

Key insight: @decorator syntax is equivalent to:
    function = decorator(function)
"""


def my_decorator(func):
    """Basic decorator that overrides the original function's behavior.
    
    This is the simplest form of a decorator. It takes a function as input
    and returns a new function (wrapper) that may add, remove, or modify
    the original function's behavior.
    
    Args:
        func (callable): The function to be decorated
    
    Returns:
        wrapper (callable): A new function that replaces the original
    
    Example:
        When you apply @my_decorator to a function, that function's
        name and behavior are replaced with the wrapper's.
    """
    
    def wrapper():
        """Wrapper function that replaces the original function.
        
        In this simple example, the wrapper completely ignores the
        original function and returns a custom string instead.
        This demonstrates how decorators can completely modify
        what a function does.
        
        Returns:
            str: A spaced-out version of "Fibonacci"
        """
        # Note: In this example, we don't actually call func()
        # The original function is replaced entirely
        return "F-I-B-O-N-A-C-C-I"
    
    return wrapper


# Applying the decorator using @ syntax
@my_decorator
def pfib():
    """Return Fibonacci string.
    
    Warning: This docstring is replaced by the wrapper's when decorated.
    See decorator_metadata.py for how to preserve function metadata.
    """
    return "Fibonacci"


# When we call pfib(), we're actually calling the wrapper function
print(f"Result: {pfib()}")


# ============================================================================
# DECORATOR TEMPLATE - Use this as a blueprint for creating decorators
# ============================================================================

def decorator_template(func):
    """Template for creating custom decorators.
    
    This shows the basic structure of most decorators you'll create.
    """
    
    def wrapper(*args, **kwargs):
        """Wrapper function that can handle any function signature.
        
        The *args and **kwargs allow the wrapper to accept any arguments
        and pass them to the original function.
        """
        # Code to run BEFORE calling the original function
        print(f"Before calling {func.__name__}")
        
        # Call the original function and capture its result
        result = func(*args, **kwargs)
        
        # Code to run AFTER calling the original function
        print(f"After calling {func.__name__}")
        
        # Return the result (or a modified version of it)
        return result
    
    return wrapper


# ============================================================================
# ADDITIONAL EXAMPLES
# ============================================================================

@decorator_template
def greet(name):
    """Example function showing decorator in action."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Demonstrate the decorator template
    result = greet("Alice")
    print(f"Final result: {result}\n")
