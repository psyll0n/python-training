#!/usr/bin/env python3
"""decorator_timing_func.py - Performance timing decorator implementation.

This module demonstrates:
- Creating a decorator to measure function execution time
- Using functools.wraps to preserve function metadata
- Working with *args and **kwargs in decorators
- Practical use case: timing recursive Fibonacci

The @timer decorator can be applied to any function to measure
its execution time with nanosecond precision.
"""

from time import perf_counter
from functools import wraps


def timer(func):
    """Decorator that measures and prints function execution time.
    
    Args:
        func: The function to be timed
    
    Returns:
        wrapper: The decorated function that includes timing
    
    Example:
        @timer
        def my_function(x):
            return x ** 2
    
    Note:
        Uses perf_counter() for high-resolution timing.
        Preserves original function metadata via @wraps.
    """
    
    @wraps(func)  # Preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        """Wrapper function that adds timing around the original function.
        
        Args:
            *args: Positional arguments passed to decorated function
            **kwargs: Keyword arguments passed to decorated function
        
        Returns:
            The result of the decorated function
        """
        # Record start time with high precision
        start = perf_counter()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Record end time
        end = perf_counter()
        
        # Calculate duration
        duration = end - start
        
        # Format and print timing information
        arg = str(*args)
        print(f"{func.__name__}({arg}) = {result} -> {duration:.8f} seconds")
        print(f"Duration: {duration:.8f} seconds")
        
        return result

    return wrapper


@timer
def fib(n):
    """Calculate the nth Fibonacci number recursively.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Note:
        This is an intentionally inefficient recursive implementation
        to demonstrate the timing decorator. For n>30, this becomes
        very slow due to exponential time complexity O(2^n).
    
    Time Complexity:
        O(2^n) - exponential (inefficient for large n)
    
    Space Complexity:
        O(n) - due to recursion call stack
    """
    if n < 2:
        return n
    else:
        # Recursive calls - each fib() call triggers the timer!
        return fib(n - 1) + fib(n - 2)


# Calculate and time the 20th Fibonacci number
# Warning: This will make many recursive calls, each timed separately
fib(20)
