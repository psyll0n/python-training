#!/usr/bin/env python3
"""decorator_function3.py - Understanding decorator execution order.

This module demonstrates:
- When decorator code executes (at definition time vs call time)
- The order of execution when decorators are applied
- Print statements that trace the execution flow
- How decorators are evaluated at function definition, not invocation

Key Insight:
    Decorators execute in TWO phases:
    1. DEFINITION TIME: When @F1 is applied to F3
    2. CALL TIME: When the decorated function F3() is actually called

Expected Output Trace:
    A (decorator application starts)
    D (decorator application ends)
    B (wrapper calls, before original)
    E (original function executes)
    C (wrapper ends, after original)
"""


def F1(f):
    """Decorator that demonstrates execution at definition time.
    
    This decorator shows when code executes:
    - Print "A" executes immediately when the decorator is applied
    - The function definition happens next
    - Print "D" executes immediately after the function is defined
    - F2 (the wrapper) is only called later when F3() is invoked
    
    Args:
        f (callable): Function to be decorated (F3)
    
    Returns:
        callable: The wrapper function F2
    
    Timeline:
        - "A" prints at DEFINITION TIME
        - "D" prints at DEFINITION TIME
        - "B", "E", "C" print at CALL TIME
    """
    # This executes at DEFINITION TIME
    print("A")

    def F2():
        """Wrapper function that executes at CALL TIME.
        
        This function is only executed when you actually call F3().
        It adds behavior before and after calling the original F3.
        
        Execution:
            1. Print "B" (before calling original)
            2. Call f() (the original F3)
            3. Print "C" (after calling original)
        """
        print("B")
        # Call the original function
        f()
        print("C")

    # This also executes at DEFINITION TIME (after F2 is defined)
    print("D")
    return F2


# When Python encounters @F1, it immediately:
# 1. Calls F1(F3) - this prints "A" and "D"
# 2. Sets F3 = F1(F3) - now F3 is actually F2
# The original F3 is not called yet!

@F1
def F3():
    """Original function being decorated.
    
    This function is not called during decoration.
    It only executes when someone calls F3().
    
    At decoration time, the decorator F1 is applied,
    which immediately prints "A" and "D".
    """
    # This executes at CALL TIME (when F3() is invoked)
    print("E")


# ============================================================================
# EXECUTION: Now we actually call the decorated function
# ============================================================================

print("\n--- Calling F3() (the decorated function) ---\n")
F3()


# ============================================================================
# ANALYSIS
# ============================================================================

print("\n" + "="*70)
print("EXECUTION ANALYSIS")
print("="*70)
print("""
Decorator Definition Phase (lines: @F1 -> def F3):
    1. F1(F3) is called by Python
    2. F1 prints "A"
    3. F2 is defined inside F1 (not called yet)
    4. F1 prints "D"
    5. F1 returns F2
    6. F3 name is bound to F2 object
    Result: "A" and "D" are printed, but original F3 body is NOT executed

Decorated Function Call Phase (line: F3()):
    1. F3() is invoked (which is now F2!)
    2. F2 prints "B"
    3. F2 calls f() (the original F3 function object)
    4. Original F3 prints "E"
    5. F2 continues and prints "C"
    Result: "B", "E", "C" are printed in that order

Key Lesson:
    Understanding when decorator code executes is critical for:
    - Debugging decorator behavior
    - Avoiding side effects at import time
    - Writing efficient decorators
""")
