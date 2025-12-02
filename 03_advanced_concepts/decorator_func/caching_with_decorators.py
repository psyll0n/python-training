#!/usr/bin/env python3
# Using caching during the Fibonacci sequence function calls to speed up the calculations.

from time import perf_counter
from functools import wraps, lru_cache


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f"{func.__name__}({arg} = {result} -> {duration:.8f} seconds")
        return result

    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib(18)
