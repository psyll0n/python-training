#!/usr/bin/env python3
"""decorator_using_args_kwargs.py - Flexible decorators with *args/**kwargs.

This module demonstrates:
- Creating flexible decorators that work with any function signature
- Using *args and **kwargs in decorators
- Preserving function metadata with @wraps
- The universal decorator template

Why *args and **kwargs?

Without them, decorators only work with functions that have specific signatures:
    @my_decorator
    def func1():              # Works
        pass
    
    @my_decorator
    def func2(x, y):          # Breaks! Signature mismatch
        return x + y

With them, decorators work with any function:
    @my_decorator
    def func1():              # Works
        pass
    
    @my_decorator
    def func2(x, y):          # Works! *args, **kwargs handle any signature
        return x + y

This is the standard, recommended approach for all decorators.
"""

from functools import wraps


def decorator(func):
    """Universal decorator template using *args and **kwargs.
    
    This is the recommended pattern for creating decorators.
    It works with any function, regardless of signature.
    
    Args:
        func (callable): The function to be decorated
    
    Returns:
        callable: Wrapper function that can handle any signature
    
    Pattern:
        1. Accept *args and **kwargs in the wrapper
        2. Pass them through to the original function
        3. This makes the decorator universal
    
    Benefits:
        - Works with any function signature
        - No need to know in advance what arguments the function takes
        - Clean, simple, and reliable
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Universal wrapper that handles any function signature.
        
        Args:
            *args: Positional arguments for the decorated function
                   Can be any number of arguments
                   Example: func(1, 2, 3) -> *args = (1, 2, 3)
            
            **kwargs: Keyword arguments for the decorated function
                      Can be any key-value pairs
                      Example: func(x=1, y=2) -> **kwargs = {'x': 1, 'y': 2}
        
        Returns:
            The result of calling the decorated function
        
        Process:
            1. Perform pre-processing (optional)
            2. Call func(*args, **kwargs) to invoke original function
            3. Perform post-processing (optional)
            4. Return the result
        """
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result

    return wrapper


@decorator
def func():
    """Simple function with no arguments."""
    pass


# ============================================================================
# EXAMPLES: Demonstrating Flexibility
# ============================================================================

print("="*70)
print("DECORATOR FLEXIBILITY WITH *args/**kwargs")
print("="*70)

# Example 1: Function with no arguments
@decorator
def greet():
    """Function with no arguments."""
    return "Hello!"

print("\nExample 1 - No arguments:")
print(f"greet() = {greet()}")

# Example 2: Function with positional arguments
@decorator
def add(x, y):
    """Function with two positional arguments."""
    return x + y

print("\nExample 2 - Positional arguments:")
print(f"add(5, 3) = {add(5, 3)}")

# Example 3: Function with keyword arguments
@decorator
def greet_person(name, greeting="Hello"):
    """Function with both positional and keyword arguments."""
    return f"{greeting}, {name}!"

print("\nExample 3 - Mixed arguments:")
print(f"greet_person('Alice') = {greet_person('Alice')}")
print(f"greet_person('Bob', greeting='Hi') = {greet_person('Bob', greeting='Hi')}")

# Example 4: Function with *args
@decorator
def sum_all(*numbers):
    """Function that accepts variable number of arguments."""
    return sum(numbers)

print("\nExample 4 - Variable arguments:")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# Example 5: Function with **kwargs
@decorator
def create_person(**details):
    """Function that accepts keyword arguments."""
    return details

print("\nExample 5 - Keyword arguments:")
print(f"create_person(name='Alice', age=30, city='NYC') = {create_person(name='Alice', age=30, city='NYC')}")


# ============================================================================
# PRACTICAL DECORATOR: Logging with Flexible Arguments
# ============================================================================

def logging_decorator(func):
    """Practical decorator that logs function calls with any signature.
    
    This demonstrates a real-world use of *args/**kwargs in decorators.
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nCalling {func.__name__}")
        print(f"  Arguments: {args}")
        print(f"  Keyword Arguments: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"  Result: {result}")
        return result
    
    return wrapper


@logging_decorator
def multiply(x, y, scale=1):
    """Multiply two numbers by an optional scale."""
    return (x * y) * scale


print("\n" + "="*70)
print("PRACTICAL EXAMPLE: Logging Decorator")
print("="*70)
multiply(5, 3)
multiply(5, 3, scale=2)


# ============================================================================
# DECORATOR TEMPLATE SUMMARY
# ============================================================================

print("\n" + "="*70)
print("UNIVERSAL DECORATOR TEMPLATE")
print("="*70)
print("""
Use this template for all your decorators:

    from functools import wraps
    
    def my_decorator(func):
        \"\"\"Comprehensive decorator docstring.\"\"\"
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            \"\"\"Wrapper with flexible argument handling.\"\"\"
            
            # Pre-processing (before calling original)
            print(f\"Calling {func.__name__}\")
            
            # Call the original function
            result = func(*args, **kwargs)
            
            # Post-processing (after calling original)
            print(f\"Returned: {result}\")
            
            return result
        
        return wrapper
    
    @my_decorator
    def my_func(x, y, z=10):
        return x + y + z

Key Points:
    1. Always use @wraps to preserve metadata
    2. Use *args, **kwargs for flexibility
    3. Pass them through to the original function: func(*args, **kwargs)
    4. This single pattern works for ALL functions
    5. No need to write different decorators for different signatures
""")
