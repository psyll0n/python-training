#!/usr/bin/env python3
"""decorator_function2.py - Performance timing decorator.

This module demonstrates:
- Creating a decorator that measures function execution time
- Using the time module to capture timing data
- Calculating and reporting performance metrics
- Practical use case: measuring computation time

Note:
    This example uses time.time() which is suitable for most cases.
    For higher precision, use time.perf_counter() (see decorator_timing_func.py).
"""

import time


def elapsed_time(f):
    """Decorator that measures and prints function execution time.
    
    This decorator captures the time before and after function execution
    and calculates the elapsed time in milliseconds.
    
    Args:
        f (callable): The function to be timed
    
    Returns:
        callable: Wrapper function that adds timing functionality
    
    Note:
        The wrapper does not return the original function's result.
        This is improved in decorator_timing_func.py.
    """
    
    def wrapper():
        """Wrapper that times the original function's execution.
        
        Measurement steps:
            1. t1 = time.time()     # Start timing
            2. f()                  # Execute original function
            3. t2 = time.time()     # Stop timing
            4. Calculate: (t2 - t1) * 1000 for milliseconds
        """
        # Record the current time (in seconds since epoch)
        t1 = time.time()
        
        # Execute the original function
        f()
        
        # Record the time after execution
        t2 = time.time()
        
        # Calculate elapsed time and convert to milliseconds
        elapsed = (t2 - t1) * 1000
        print(f"Elapsed time: {elapsed:.2f} ms")

    return wrapper


@elapsed_time
def big_sum():
    """Compute the sum of integers from 0 to 999,999.
    
    This function is computationally expensive enough to measure timing.
    The decorator will measure how long this takes to execute.
    
    Steps:
        1. Create empty list
        2. Add 1 million numbers to the list
        3. Sum all numbers in the list
        4. Print the result
    
    Time Complexity: O(n) where n = 1,000,000
    Space Complexity: O(n) for storing all numbers
    """
    # Create a list to store numbers
    num_list = []
    
    # Add 1 million numbers to the list
    for num in range(0, 1000000):
        num_list.append(num)
    
    # Calculate and print the sum
    print(f"Big sum: {sum(num_list)}")


def main():
    """Main function demonstrating the timing decorator.
    
    Calls the decorated big_sum function, which will:
    1. Execute the sum computation
    2. Automatically measure execution time
    3. Print the result and timing information
    """
    big_sum()


if __name__ == "__main__":
    print("Demonstrating execution time measurement:")
    main()
    
    # Additional example with multiple runs
    print("\nRunning again to verify consistency:")
    big_sum()
