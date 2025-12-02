#!/usr/bin/env python3

from functools import update_wrapper


class Count:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Current count: {self.count}")
        result = self.func(*args, **kwargs)
        return result


@Count
def fib(n):
    """Return the Fibonacci sequence."""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib(10)
