#!/usr/bin/env python3
"""decorator_classes.py - Class-based decorators using __call__ method.

This module demonstrates:
- Creating decorators using classes instead of functions
- Using the __call__ method to make classes callable
- Maintaining state in class-based decorators
- Logging function calls with custom classes
- Extending decorators through inheritance

Comparison: Functions vs Classes for Decorators

Function-based decorators:
    - Simple and elegant
    - Good for single-responsibility decorators
    - Limited state management

Class-based decorators:
    - Can maintain state across calls
    - More features through methods
    - Easier to extend with inheritance
    - Good for complex decorators

When to use class-based decorators:
    - When you need to maintain state
    - When you need to inherit and extend
    - When you need methods beyond decoration
    - Complex logging or monitoring requirements
"""

from functools import update_wrapper


class logit(object):
    """A simple decorator class for logging function calls.
    
    This class-based decorator demonstrates:
    - Using __init__ to store the decorated function
    - Using __call__ to make the class instance callable
    - Maintaining state (logfile name)
    - Extensibility through inheritance
    
    Attributes:
        _logfile (str): Path to log file (class attribute)
        func (callable): The decorated function (instance attribute)
    """
    
    _logfile = "out.log"  # Class attribute: default log file

    def __init__(self, func):
        """Initialize the decorator with the function to be decorated.
        
        Args:
            func (callable): Function to be decorated
        
        Why update_wrapper?
            Preserves the original function's metadata (__name__, __doc__, etc.)
            Similar to functools.wraps for class-based decorators.
        """
        # Store the decorated function
        self.func = func
        
        # Copy metadata from func to self (like functools.wraps)
        update_wrapper(self, func)

    def __call__(self, *args):
        """Make the decorator instance callable.
        
        This method is invoked when you call the decorated function.
        
        Args:
            *args: Arguments passed to the decorated function
        
        Returns:
            The result of calling the original function
        
        Process:
            1. Create a log message with function name
            2. Write the message to the log file
            3. Send a notification (can be overridden in subclasses)
            4. Call and return the original function
        """
        # Create a descriptive log message
        log_string = self.func.__name__ + " was called."
        
        # Append the message to the log file
        with open(self._logfile, "a") as opened_file:
            # Now we log to the specified logfile.
            opened_file.write(log_string + "\n")
        
        # Now, send a notification.
        self.notify()

        # Return base function.
        return self.func(*args)

    def notify(self):
        """Send a notification when function is called.
        
        This method is called every time the decorated function is invoked.
        In the base logit class, this does nothing.
        In subclasses (like email_logit), this can be overridden
        to send emails, slack messages, etc.
        """
        # Logit only logs, no more.
        pass


# Set the default log file name
logit._logfile = "out.log"  # if change logfile.


@logit
def myfunc1():
    """Example function that will be logged."""
    pass


myfunc1()


class email_logit(logit):
    """Extended decorator that sends emails on function calls.
    
    This class demonstrates decorator extensibility through inheritance.
    It inherits from logit and overrides the notify() method to send emails.
    
    Attributes:
        email (str): Admin email address for notifications
    """

    def __init__(self, func, email="admin@myproject.com"):
        """Initialize with optional email parameter.
        
        Note: The original code had __init_ (single underscore) which prevented
        proper override. This corrected version uses __init__.
        
        Args:
            func (callable): Function to be decorated
            email (str): Email address for notifications
        """
        super(email_logit, self).__init__(func)
        self.email = email

    def notify(self):
        """Send an email notification when function is called.
        
        In a real application, this would use smtplib or a mail service
        to send emails to the administrator when the decorated function
        is called. This is useful for monitoring critical functions.
        
        Note: Email sending not implemented in this example.
        """
        # Send an email to self.email.
        # Will not be implemented here.
        pass


# ============================================================================
# ADVANTAGES OF CLASS-BASED DECORATORS
# ============================================================================

print("="*70)
print("ADVANTAGES OF CLASS-BASED DECORATORS")
print("="*70)
print("""
1. State Management:
   - Can maintain state across multiple calls
   - Example: count calls, track timing, accumulate statistics

2. Inheritance:
   - Extend functionality through subclassing
   - Example: email_logit extends logit

3. Methods:
   - Can have helper methods
   - Example: notify() can be overridden

4. Attributes:
   - Can store configuration
   - Example: email address in email_logit

5. Extensibility:
   - Easy to add features without modifying original

Comparison with Functions:

Function-based:
    @timer
    def my_func(): pass
    
    - Simple and readable
    - Functional programming style
    - Limited state management

Class-based:
    @Timer(output="json")
    def my_func(): pass
    
    - More powerful
    - OOP style
    - Better for complex scenarios
""")
