#!/usr/bin/env python3
"""html_decorator_styling.py - Chaining decorators for HTML styling.

This module demonstrates:
- Multiple decorators applied to a single function
- Decorator chaining and execution order
- HTML element wrapping with decorators
- How decorators compose together

Decorator Chaining:

When you apply multiple decorators:

    @bold
    @italics
    def text():
        return "Fibonacci"

Python applies them bottom-to-top during definition:
    1. First: text = italics(text)
    2. Then: text = bold(italicized_text)

Execution order is top-to-bottom:
    1. bold() executes first (outer decorator)
    2. italics() executes second (inner decorator)
    3. Original text() executes last (innermost)

Result: <b><i>Fibonacci</i></b>

This creates nested HTML tags through decorator composition.
"""

from functools import wraps


def bold(func):
    """Decorator that wraps return value in <b> tags.
    
    Adds bold HTML formatting to the function's return value.
    
    Args:
        func (callable): Function to be decorated
    
    Returns:
        callable: Wrapper that adds bold tags
    """

    @wraps(func)
    def wrapper():
        """Return html bold tags"""
        result = "<b>" + func() + "</b>"
        return result

    return wrapper


def italics(func):
    """Decorator that wraps return value in <i> tags.
    
    Adds italics HTML formatting to the function's return value.
    
    Args:
        func (callable): Function to be decorated
    
    Returns:
        callable: Wrapper that adds italics tags
    """

    @wraps(func)
    def wrapper():
        """Return html italics tags"""
        result = "<i>" + func() + "</i>"
        return result

    return wrapper


@bold
@italics
def printfib():
    """Return Fibonacci with bold and italics formatting.
    
    This demonstrates decorator chaining:
    - @italics is applied first (inner)
    - @bold is applied second (outer)
    - Execution: bold() -> italics() -> printfib()
    - Result: <b><i>Fibonacci</i></b>
    """
    return "Fibonacci"


# Execute the decorated function
result = printfib()
print(f"Result: {result}")
print(f"Expected: <b><i>Fibonacci</i></b>")

# ============================================================================
# DEMONSTRATION: Decorator Execution Order
# ============================================================================

print("\n" + "="*70)
print("DECORATOR CHAINING ANALYSIS")
print("="*70)

print("""
Code:
    @bold
    @italics
    def printfib():
        return "Fibonacci"

Definition Phase:
    1. @italics is applied: printfib = italics(printfib)
    2. @bold is applied: printfib = bold(italics_wrapper)
    3. Now printfib refers to bold_wrapper

Call Phase (when printfib() is called):
    1. bold_wrapper executes
    2. bold_wrapper calls italics_wrapper
    3. italics_wrapper calls original function
    4. Original function returns "Fibonacci"
    5. italics_wrapper wraps it: "<i>Fibonacci</i>"
    6. bold_wrapper wraps it: "<b><i>Fibonacci</i></b>"

Final Result: <b><i>Fibonacci</i></b>

Key Insight:
    The ORDER of decorators matters!
    @bold @italics != @italics @bold
""")

# ============================================================================
# EXAMPLE: Reversed Order
# ============================================================================

@italics
@bold
def printfib2():
    """Same function, different decorator order."""
    return "Fibonacci"

print(f"\nReversed order (@italics @bold):")
print(f"Result: {printfib2()}")
print(f"Expected: <i><b>Fibonacci</b></i>")
