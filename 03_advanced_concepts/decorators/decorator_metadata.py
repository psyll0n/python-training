#!/usr/bin/env python3
"""decorator_metadata.py - Preserving function metadata with @wraps.

This module demonstrates:
- The problem: decorators lose function metadata
- The solution: using functools.wraps to preserve metadata
- What metadata is preserved by @wraps
- Why preserving metadata is important

The Problem:
    When a decorator wraps a function, the wrapper replaces the original.
    This means the function's __name__, __doc__, and other attributes
    are lost, replaced by the wrapper's metadata.

The Solution:
    functools.wraps copies metadata from the wrapped function to the
    wrapper, preserving important attributes like __name__ and __doc__.

Preserved Attributes:
    - __name__: Function name
    - __doc__: Docstring
    - __module__: Module name
    - __qualname__: Qualified name
    - __annotations__: Type hints
    - __dict__: Function attributes
"""

from functools import wraps


def make_posh(func):
    """Decorator that wraps content in ASCII boxes.
    
    This decorator demonstrates the importance of using @wraps to
    preserve the original function's metadata.
    
    Args:
        func (callable): Function to be decorated
    
    Returns:
        callable: Wrapper function that displays content in a box
    
    Without @wraps in the wrapper:
        - wrapper.__name__ would be 'wrapper'
        - wrapper.__doc__ would be 'This is the wrapper function.'
    
    With @wraps(func):
        - wrapper.__name__ would be 'printfib' (preserved)
        - wrapper.__doc__ would be 'Print the Fibonacci sequence.' (preserved)
    """

    @wraps(func)  # This is crucial! It preserves func's metadata
    def wrapper():
        """This docstring is replaced by the wrapped function's docstring.
        
        With @wraps(func), this wrapper's docstring is replaced by func's.
        This is intentional and desired behavior - we want to preserve
        the original function's documentation.
        """
        # Add decoration before execution
        print("+-------+")
        print("|       |")
        
        # Call the original function and capture result
        result = func()
        
        # Display the result
        print(result)
        
        # Add decoration after execution
        print("|       |")
        print("+-------+")
        return result

    # Before @wraps, you might manually copy metadata like this:
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    # The @wraps decorator does all of this automatically!
    return wrapper


@make_posh
def printfib():
    """Print the Fibonacci sequence.
    
    This docstring is preserved by @wraps(func).
    Without @wraps, this would be lost!
    """
    return "Fibonacci"


# ============================================================================
# DEMONSTRATION: Metadata Preservation
# ============================================================================

print("=== Demonstrating @wraps ===\n")

# Call the decorated function
printfib()

# Verify that metadata is preserved
print(f"\n--- Metadata Verification ---")
print(f"Function name: {printfib.__name__}")
print(f"Expected: printfib ✓")

print(f"\nFunction docstring: {printfib.__doc__}")
print(f"Expected: 'Print the Fibonacci sequence.' ✓")

print(f"\nFunction module: {printfib.__module__}")


# ============================================================================
# COMPARISON: Decorator without @wraps
# ============================================================================

print("\n" + "="*70)
print("COMPARISON: Decorator without @wraps")
print("="*70)


def make_posh_without_wraps(func):
    """Decorator WITHOUT @wraps - metadata is lost.
    
    This demonstrates what happens when @wraps is NOT used.
    """
    def wrapper():
        print("+-------+")
        print("|       |")
        result = func()
        print(result)
        print("|       |")
        print("+-------+")
        return result

    return wrapper


@make_posh_without_wraps
def printfib2():
    """Print the Fibonacci sequence (no @wraps)."""
    return "Fibonacci"


print(f"\nWithout @wraps:")
print(f"Function name: {printfib2.__name__}")
print(f"Problem: It's 'wrapper' instead of 'printfib2'! ✗")

print(f"\nFunction docstring: {printfib2.__doc__}")
print(f"Problem: The original docstring is lost! ✗")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "="*70)
print("SUMMARY: Why @wraps Matters")
print("="*70)
print("""
Benefits of using @wraps:
    1. Preserved documentation: Docstrings appear in help()
    2. Better debugging: Error messages show original function name
    3. IDE support: Autocomplete and type hints work correctly
    4. Introspection: Code that inspects function metadata works properly
    5. Profiling: Performance tools identify the correct function

Best Practice:
    Always use @wraps in your decorators!
    
    from functools import wraps
    
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Your decorator code here
            return func(*args, **kwargs)
        return wrapper
""")
