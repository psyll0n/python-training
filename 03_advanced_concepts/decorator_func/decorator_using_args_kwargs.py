#!/usr/bin/env python3
# Docorator template using arguments and keyword arguments.


from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result

    return wrapper


@decorator
def func():
    pass
