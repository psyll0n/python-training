#!/usr/bin/env python3
"""generator_function.py - Demonstrates Python generator functions.

Generators are functions that use 'yield' instead of 'return' to produce
a sequence of values lazily (one at a time, on demand).

Key Concepts:
- yield: Pauses function and returns a value; resumes on next() call
- Generators maintain state between calls
- Memory efficient: doesn't store entire sequence in memory
- Can represent infinite sequences

Advantages over Lists:
- Lower memory usage (especially for large sequences)
- Can represent infinite sequences
- Only compute values as needed (lazy evaluation)

Generator Protocol:
- next(generator): Get next value
- StopIteration: Raised when generator is exhausted
"""

import time

# Get starting number from user
n = int(input("Please, enter a number to start the countdown: "))


def countdown(n):
    """Generator function that yields countdown values from n to 1.
    
    This is a generator (not a regular function) because it uses 'yield'.
    Each call to next() resumes execution after the last yield.
    
    Args:
        n (int): Starting number for countdown
    
    Yields:
        int: Next number in countdown sequence
    
    Example:
        >>> gen = countdown(3)
        >>> next(gen)
        3
        >>> next(gen)
        2
        >>> next(gen)
        1
        >>> next(gen)  # Raises StopIteration
    
    How it works:
    1. Function starts, prints message
    2. First yield returns n
    3. Function pauses, state saved
    4. next() call resumes after yield
    5. Decrements n, loops back to yield
    6. When n reaches 0, function ends (StopIteration)
    """
    print("Starting to count down from", n, "...")
    
    # Loop continues as long as n > 0
    while n > 0:
        yield n  # Pause here, return n, wait for next() call
        n -= 1   # Resume here on next() call


# ===== Using the Generator =====

# Create the generator object (doesn't execute function yet)
c = countdown(n)

# Iterate through the countdown
# Each iteration calls next(c) to get the next value
for i in range(0, n):
    print(next(c))  # Get next value from generator
    time.sleep(1)   # Wait 1 second between numbers

print("Done!")

# Note: Could also iterate directly over the generator:
# for num in countdown(n):
#     print(num)
#     time.sleep(1)
