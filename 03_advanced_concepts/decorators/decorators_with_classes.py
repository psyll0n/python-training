#!/usr/bin/env python3
"""decorators_with_classes.py - Class-based decorator with call counting.

This module demonstrates:
- Creating a class-based decorator that maintains state
- Using update_wrapper to preserve function metadata
- Tracking function call statistics
- The __call__ method for making decorator instances callable

Key Difference from Function Decorators:

Function Decorators:
    - Stateless (each invocation starts fresh)
    - Simple and elegant
    - Good for most use cases

Class Decorators:
    - Can maintain state across calls
    - Perfect for tracking statistics
    - More powerful for complex scenarios

This Example: Call Counter
    - Tracks how many times a decorated function is called
    - Maintains a count as an instance attribute
    - Demonstrates practical use of class-based decorators
"""

from functools import update_wrapper


class Count:
    """A decorator class that counts function calls.
    
    This decorator maintains a count of how many times the decorated
    function has been called. This demonstrates the power of class-based
    decorators for maintaining state.
    
    Attributes:
        func (callable): The decorated function
        count (int): Number of times the function has been called
    """
    
    def __init__(self, func):
        """Initialize the counter decorator.
        
        Args:
            func (callable): Function to be decorated
        
        Why update_wrapper?
            Copies metadata from func to self (like functools.wraps).
            Ensures self.__name__, self.__doc__ match the original function.
        """
        # Copy metadata from the function to this decorator instance
        update_wrapper(self, func)
        
        # Store the decorated function
        self.func = func
        
        # Initialize call counter
        self.count = 0

    def __call__(self, *args, **kwargs):
        """Make the decorator instance callable.
        
        This is called when you invoke the decorated function.
        It increments the counter and calls the original function.
        
        Args:
            *args: Positional arguments for the decorated function
            **kwargs: Keyword arguments for the decorated function
        
        Returns:
            The result of calling the original function
        """
        # Increment counter
        self.count += 1
        
        # Print current count
        print(f"Current count: {self.count}")
        
        # Call the original function and return result
        result = self.func(*args, **kwargs)
        return result


@Count
def fib(n):
    """Calculate the nth Fibonacci number.
    
    This function is decorated with @Count to track how many times
    it's been called. Notice the count increases with each call.
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: The nth Fibonacci number
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# ============================================================================
# DEMONSTRATION
# ============================================================================

print("="*70)
print("CLASS-BASED DECORATOR: Call Counter")
print("="*70)

print(f"\nCalling fib(10)...")
result = fib(10)

print(f"\nResult: fib(10) = {result}")
print(f"Total calls made: {fib.count}")

# ============================================================================
# ANALYSIS: Understanding the Recursion
# ============================================================================

print("\n" + "="*70)
print("CALL COUNTING WITH RECURSIVE FUNCTIONS")
print("="*70)

print(f"""
Explanation:
  fib(10) requires many recursive calls
  Each recursive call increments the counter
  The counter shows total number of function invocations
  Not just the number of times we explicitly called fib()!

For fib(10), the counter shows: {fib.count}
This represents all recursive calls made during computation.
""")
