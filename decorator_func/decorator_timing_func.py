#!/usr/bin/env python3


from time import perf_counter
from functools import wraps

# Measuring time it takes to execute a function.
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f"{func.__name__}({arg}) = {result} -> {duration:.8f} seconds")
        print(f"Duration: {duration:.8f} seconds")
        return result

    return wrapper


@timer
def fib(n):
    """Return the value from the Fibonacci sequence"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib(20)
