#!/usr/bin/env python3
"""decorator_function.py - Creating custom decorators from scratch.

This module demonstrates:
- The structure and flow of creating a simple decorator
- How decorators intercept function calls
- Adding behavior before and after function execution
- Basic decorator pattern: decorator takes func, returns wrapper

Key Pattern:
    Decorator (takes func) -> Wrapper (replaces func) -> executes with added behavior
"""


def f1(f):
    """Simple decorator that adds print statements before and after execution.
    
    Args:
        f (callable): Function to be decorated
    
    Returns:
        callable: Wrapper function with added behavior
    
    How it works:
        1. Takes function f as input
        2. Defines wrapper function f2 that wraps f
        3. Returns f2, which now replaces f
    """
    
    def f2():
        """Wrapper function that adds behavior around the original.
        
        This wrapper:
        1. Prints a message before calling the original function
        2. Calls the original function f()
        3. Prints a message after the original function returns
        """
        print("This is before the function call.")
        f()
        print("This is after the function call.")

    return f2


@f1
def f3():
    """Original function being decorated.
    
    When @f1 decorator is applied, this function is wrapped.
    The decorator adds print statements before and after execution.
    """
    print("This is f3")


# Call the decorated function
# Note: f3 is now actually f2 (the wrapper)
f3()
