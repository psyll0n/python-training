#!/usr/bin/env python3

# Decorator function use cases.

# Use case 1. Decorators can help to check whether someone is authorized to use an endpoint in a
# web application. They are extensively used in Flask web framework and Django.


from functools import wraps


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated


# Use case 2. Decorators can be used to add logging to a function.


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)


# Use case 3. Nesting decorators within a Function.


def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open a logfile, write log_string, close logfile
            with open(logfile, "a") as opened_file:
                # Now we log to the specified logfile.
                opened_file.write(log_string + "\n")
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


@logit(logfile="func2.log")
def myfunc2():
    pass
