#!/usr/bin/env python3
"""decorators_usecases.py - Practical real-world use cases for decorators.

This module demonstrates three important decorator patterns:

1. AUTHENTICATION & AUTHORIZATION
   - Checking permissions before function execution
   - Used in web frameworks (Flask, Django)
   - Protecting sensitive functions

2. LOGGING & MONITORING
   - Recording function calls
   - Tracking function execution
   - Debugging and auditing

3. PARAMETERIZED DECORATORS
   - Decorators that accept arguments
   - Creating flexible, configurable decorators
   - Dynamic behavior based on parameters

These patterns are fundamental to modern Python applications,
especially web frameworks and libraries.
"""

from functools import wraps


# ============================================================================
# USE CASE 1: AUTHENTICATION & AUTHORIZATION
# ============================================================================

def requires_auth(f):
    """Decorator that requires authentication before function execution.
    
    This pattern is extensively used in:
    - Flask web framework: @app.route(), @login_required
    - Django framework: @permission_required, @login_required
    - API endpoints: @token_required, @api_key_required
    
    Args:
        f (callable): Function that requires authentication
    
    Returns:
        callable: Wrapper that checks authentication first
    
    Process:
        1. Check if user is authenticated
        2. If not authenticated, trigger authentication
        3. If authenticated, execute the function
    
    Note:
        This is a simplified example. Real implementations would:
        - Check session tokens or cookies
        - Verify JWT tokens
        - Check user roles and permissions
        - Handle authentication failures
    """
    
    @wraps(f)
    def decorated(*args, **kwargs):
        """Wrapper that verifies authentication before execution.
        
        Args:
            *args: Arguments for the decorated function
            **kwargs: Keyword arguments for the decorated function
        
        Returns:
            Result of the decorated function if authenticated
        """
        # Check authentication (simplified - normally from request context)
        # In real apps: auth = request.authorization
        # For this example, we'll skip the actual check
        
        # auth = request.authorization
        # if not auth or not check_auth(auth.username, auth.password):
        #     authenticate()
        
        # If authenticated, execute function
        return f(*args, **kwargs)

    return decorated


# ============================================================================
# USE CASE 2: LOGGING & MONITORING
# ============================================================================

def logit(func):
    """Decorator that logs function calls.
    
    Simple logging decorator that records when a function is called.
    
    Uses:
    - Debug function execution
    - Track which functions are being used
    - Audit trail of function calls
    - Performance monitoring
    
    Args:
        func (callable): Function to be logged
    
    Returns:
        callable: Wrapper that logs the call
    
    Example:
        @logit
        def sensitive_operation(x):
            return x * 2
        
        Output:
            sensitive_operation was called
        Result: 4
    """
    
    @wraps(func)
    def with_logging(*args, **kwargs):
        """Wrapper that logs function calls.
        
        Before calling the function, prints a message indicating
        that the function was invoked. This is useful for:
        - Debugging: See which functions are running
        - Auditing: Track what operations are performed
        - Monitoring: Identify performance bottlenecks
        """
        print(f"{func.__name__} was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math with logging.
    
    Example of a function decorated with logging.
    """
    return x + x


print(f"Result: {addition_func(4)}\n")


# ============================================================================
# USE CASE 3: PARAMETERIZED DECORATORS
# ============================================================================

def logit(logfile="out.log"):
    """Decorator factory that accepts configuration parameters.
    
    This is a more advanced pattern where the decorator itself can be
    configured. Instead of decorating a function directly, you call
    the decorator factory with parameters, which returns a decorator.
    
    Args:
        logfile (str): Path to the log file (default: "out.log")
    
    Returns:
        callable: A decorator function that uses the specified logfile
    
    Why This Pattern?
    
    Without parameters:
        @logit
        def func():
            pass
        
        All decorated functions log to the same file.
    
    With parameters:
        @logit(logfile="critical.log")
        def critical_func():
            pass
        
        @logit(logfile="debug.log")
        def debug_func():
            pass
        
        Functions can use different log files!
    
    How It Works:
    
        1. logit(logfile="out.log") is called
           - Returns logging_decorator function
        2. @logging_decorator is applied to the function
           - logging_decorator is called with the function
           - Returns wrapped_function
        3. wrapped_function is what gets called
           - Uses the logfile from the outer scope (closure)
    
    Real-World Examples:
    
    Flask:
        @app.route('/api/users', methods=['POST'])
        def create_user():
            pass
    
    Django:
        @permission_required('view_reports', raise_exception=True)
        def view_reports():
            pass
    
    Rate Limiting:
        @rate_limit(max_calls=10, time_window=60)
        def api_endpoint():
            pass
    """
    
    def logging_decorator(func):
        """The actual decorator (returned by the factory).
        
        This is the decorator that gets applied to the function.
        It captures the logfile parameter from the outer scope (closure).
        
        Args:
            func (callable): Function to be decorated
        
        Returns:
            callable: Wrapped function with logging to specified file
        """
        
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            """Wrapper that logs to the specified file.
            
            This wrapper:
            1. Creates a log message with function name
            2. Prints the message to console
            3. Appends the message to the specified log file
            4. Calls the original function
            5. Returns the result
            
            The logfile is determined by the parameter passed to the decorator
            factory, demonstrating closure and parameter capture.
            """
            log_string = func.__name__ + " was called"
            print(log_string)
            
            # Append to log file
            with open(logfile, "a") as opened_file:
                # Now we log to the specified logfile.
                opened_file.write(log_string + "\n")
            
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


# Use the parameterized decorator with default parameters
@logit()
def myfunc1():
    """Function using default log file."""
    print("myfunc1 executed")


myfunc1()


# Use the parameterized decorator with custom log file
@logit(logfile="func2.log")
def myfunc2():
    """Function using custom log file."""
    print("myfunc2 executed")


myfunc2()


# ============================================================================
# SUMMARY: USE CASES
# ============================================================================

print("\n" + "="*70)
print("DECORATOR USE CASES SUMMARY")
print("="*70)
print("""
1. AUTHENTICATION & AUTHORIZATION:
   Pattern: @requires_auth, @login_required, @admin_only
   Use: Protect functions that require permissions
   Example: Web framework endpoints
   
   @login_required
   def delete_account(user_id):
       # Only logged-in users can execute
       pass

2. LOGGING & MONITORING:
   Pattern: @logit, @logger, @audit
   Use: Track function calls and behavior
   Example: Recording function execution for debugging
   
   @logit
   def database_operation():
       # All calls are logged automatically
       pass

3. PARAMETERIZED DECORATORS:
   Pattern: @decorator(param1, param2)
   Use: Create flexible, configurable decorators
   Example: Different behavior based on parameters
   
   @logit(logfile="important.log")
   def important_function():
       # Logs to specified file
       pass
   
   @logit(logfile="debug.log")
   def debug_function():
       # Logs to different file
       pass

4. CACHING/MEMOIZATION:
   Pattern: @cache, @memoize, @lru_cache
   Use: Avoid recalculating expensive operations
   
   @lru_cache(maxsize=128)
   def fibonacci(n):
       # Results are cached
       pass

5. TIMING/PERFORMANCE:
   Pattern: @timer, @profile, @benchmark
   Use: Measure function execution time
   
   @timer
   def slow_operation():
       # Execution time is measured
       pass

6. VALIDATION:
   Pattern: @validate_input, @check_permissions
   Use: Validate inputs before execution
   
   @validate_email
   def send_email(email):
       # Email is validated before sending
       pass

7. RETRY LOGIC:
   Pattern: @retry, @exponential_backoff
   Use: Automatically retry failed operations
   
   @retry(max_attempts=3, backoff=2)
   def network_request():
       # Automatically retries on failure
       pass

8. ERROR HANDLING:
   Pattern: @handle_exceptions, @catch_errors
   Use: Centralized error handling
   
   @handle_exceptions
   def risky_operation():
       # Exceptions are caught and logged
       pass
""")
