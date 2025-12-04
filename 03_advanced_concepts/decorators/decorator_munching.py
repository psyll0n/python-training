#!/usr/bin/env python3
"""decorator_munching.py - String munching decorator with parameters.

This module demonstrates:
- Parameterized decorators (decorators that accept arguments)
- Processing and modifying return values
- Decorator factories (functions that return decorators)
- Practical example: selective character replacement

String "Munching":
    In this context, "munching" means selectively replacing characters
    in a string with a placeholder character ('x').

How It Works:
    The decorator takes two parameters: start and end
    These define the range of character positions to replace
    All characters in that range are replaced with 'x'

Example:
    @munch(0, 5)
    def get_password():
        return "MyPassword123"
    
    Result: "xxxxxx
    
    This could be useful for:
    - Obfuscating sensitive information in logs
    - Hiding passwords or tokens
    - Privacy protection in output
"""

from functools import wraps


def munch(start, end):
    """Decorator factory that creates a string-munching decorator.
    
    This is a parameterized decorator - instead of directly decorating
    a function, you call the decorator with parameters first.
    
    Args:
        start (int): Starting index of characters to replace (inclusive)
        end (int): Ending index of characters to replace (inclusive)
    
    Returns:
        callable: A decorator function that munches strings
    
    Pattern:
        1. munch(start, end) is called with parameters
           - Returns do_munch decorator
        2. @do_munch decorates the function
           - Returns wrapper function
        3. wrapper() is called
           - Munches the return value
    
    Why This Pattern?
        Allows different decorator instances with different parameters.
        Without parameters, all decorated functions would munch the same range.
        With parameters, you control the munching behavior for each function.
    
    Examples:
        @munch(0, 3)      # Replace first 4 characters
        def func1():
            return "abcdefgh"  # Returns "xxxx"
        
        @munch(2, 5)      # Replace characters 2-5
        def func2():
            return "abcdefgh"  # Returns "abxxxfgh"
    """
    
    def do_munch(func):
        """The actual decorator (returned by munch factory).
        
        This is the decorator that gets applied to the function.
        It captures start and end parameters from outer scope (closure).
        
        Args:
            func (callable): Function to be decorated
        
        Returns:
            callable: Wrapper that munches the function's return value
        """
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper that munches the return value.
            
            Args:
                *args: Arguments for the decorated function
                **kwargs: Keyword arguments for the decorated function
            
            Returns:
                str: The function's return value with specified characters replaced
            
            Process:
                1. Call the original function
                2. Iterate through each character
                3. Replace characters in the specified range with 'x'
                4. Keep other characters unchanged
                5. Return the munched string
            """
            # Call the original function
            result = func(*args, **kwargs)
            
            # Build the munched string
            new_string = ""
            for index, char in enumerate(result):
                # Check if this character's index is in the munch range
                if start <= index <= end:
                    # Replace with 'x'
                    c = "x"
                else:
                    # Keep original character
                    c = char
                new_string += c
            
            return new_string

        return wrapper

    return do_munch


# ============================================================================
# EXAMPLE 1: Basic Usage
# ============================================================================

@munch(0, 10)
def fib():
    """Return Fibonacci string.
    
    The @munch(0, 10) decorator will replace characters 0-10 with 'x'.
    """
    return "Fibonacci"


print("="*70)
print("STRING MUNCHING DECORATOR")
print("="*70)

print(f"\nOriginal return value: \"Fibonacci\"")
print(f"Decorated result: \"{fib()}\"")
print(f"Range munched: 0-10 (first 11 characters)")

# ============================================================================
# EXAMPLE 2: Different Ranges
# ============================================================================

@munch(0, 3)
def password():
    """Return a password with first 4 characters munched."""
    return "SuperSecret123"

print(f"\nPassword function:")
print(f"Original: \"SuperSecret123\"")
print(f"Munched: \"{password()}\"")
print(f"Range: 0-3 (first 4 characters hidden)")

# ============================================================================
# EXAMPLE 3: Middle Range
# ============================================================================

@munch(5, 10)
def token():
    """Return a token with middle portion munched."""
    return "abc123def456ghi"

print(f"\nToken function:")
print(f"Original: \"abc123def456ghi\"")
print(f"Munched: \"{token()}\"")
print(f"Range: 5-10 (middle portion hidden)")

# ============================================================================
# EXPLANATION: Parameterized Decorators
# ============================================================================

print("\n" + "="*70)
print("PARAMETERIZED DECORATORS PATTERN")
print("="*70)

print("""
The munch decorator demonstrates a powerful pattern:
DECORATORS WITH PARAMETERS

Syntax Pattern:

    def decorator_factory(param1, param2):
        '''Factory that returns a decorator.'''
        
        def actual_decorator(func):
            '''The decorator that decorates the function.'''
            
            @wraps(func)
            def wrapper(*args, **kwargs):
                '''The wrapper that executes the logic.'''
                # Use param1 and param2 from outer scope (closure)
                result = func(*args, **kwargs)
                # Do something with param1, param2
                return result
            
            return wrapper
        
        return actual_decorator
    
    # Usage:
    @decorator_factory(param1_value, param2_value)
    def my_function():
        pass

Execution Flow:

    @munch(0, 10)
    def fib():
        return "Fibonacci"
    
    1. munch(0, 10) is called
       - Returns do_munch decorator (capturing start=0, end=10)
    
    2. @do_munch is applied to fib
       - Returns wrapper function (capturing func=fib)
    
    3. fib() is called
       - Actually calls wrapper()
       - wrapper calls original fib()
       - wrapper munches the result using start and end
    
    4. Munched result is returned

Why This Matters:

    Flexibility: Each decorated function can have different behavior
    Reusability: One decorator factory creates many specialized decorators
    Clarity: Parameters make the decorator's purpose clear
    Power: Enables complex, configurable decorators

Common Use Cases:

    Rate Limiting:
        @rate_limit(max_calls=10, time_window=60)
        def api_endpoint():
            pass
    
    Caching:
        @cache(ttl=3600)
        def expensive_query():
            pass
    
    Retries:
        @retry(max_attempts=3, backoff=2)
        def network_call():
            pass
    
    Logging:
        @log(level='DEBUG', file='app.log')
        def debug_function():
            pass
""")
