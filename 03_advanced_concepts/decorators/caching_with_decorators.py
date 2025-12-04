#!/usr/bin/env python3
"""caching_with_decorators.py - Memoization using @lru_cache decorator.

This module demonstrates:
- The @lru_cache decorator for memoization
- How caching dramatically improves recursive function performance
- Combining decorators (@lru_cache with @timer)
- Time complexity improvements with memoization

Problem:
    Without caching, the recursive Fibonacci function makes many redundant
    calculations. For fib(10), fib(5) is calculated 8 times!
    Time Complexity: O(2^n) - exponential (very slow)

Solution:
    With @lru_cache, each calculation is cached and reused.
    Time Complexity: O(n) - linear (very fast)

Performance Impact:
    fib(18) without cache: ~15 seconds
    fib(18) with cache: <0.001 seconds

LRU Cache Details:
    - LRU: Least Recently Used
    - maxsize: Maximum number of cached results
    - maxsize=None: unlimited cache
    - maxsize=128: default size
"""

from time import perf_counter
from functools import wraps, lru_cache


def timer(func):
    """Decorator that measures function execution time.
    
    Args:
        func (callable): Function to be timed
    
    Returns:
        callable: Wrapper with timing capability
    
    Note:
        Uses perf_counter() for high-resolution timing.
        Preserves original function's __name__ and __doc__.
    """
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper that times execution and returns result.
        
        Args:
            *args: Positional arguments for the decorated function
            **kwargs: Keyword arguments for the decorated function
        
        Returns:
            The result of the decorated function
        """
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        
        # Format output with argument information
        arg = str(*args)
        print(f"{func.__name__}({arg}) = {result} -> {duration:.8f} seconds")
        return result

    return wrapper


# ============================================================================
# CACHED FIBONACCI - Fast Implementation
# ============================================================================

@lru_cache(maxsize=None)
@timer
def fib(n):
    """Calculate the nth Fibonacci number with caching.
    
    Uses @lru_cache for automatic memoization.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(n) with caching (vs O(2^n) without)
    Space Complexity: O(n) for cache storage
    
    Decorator Order:
        @lru_cache is applied first (outer), then @timer (inner)
        Execution order: timer -> lru_cache -> fib
    
    Why This Order?
        Placing @lru_cache first means:
        - The cache intercepts the call
        - If cached, returns immediately without timing each call
        - If not cached, calls the timed version
        - This avoids counting cache lookup time in the timer
    
    Example:
        fib(18)
        Without cache: ~15 seconds
        With cache: <0.001 seconds (after first calculation)
    """
    if n < 2:
        return n
    else:
        # Recursive calls - with cache, each fib(n) is calculated only once
        return fib(n - 1) + fib(n - 2)


# ============================================================================
# DEMONSTRATION
# ============================================================================

print("="*70)
print("FIBONACCI CALCULATION WITH CACHING")
print("="*70)

print("\nCalculating fib(18) with @lru_cache:")
print("(Note: Each calculation is timed, but cached results are instant)\n")

result = fib(18)

print(f"\nFinal result: {result}")

# ============================================================================
# CACHE STATISTICS
# ============================================================================

print("\n" + "="*70)
print("CACHE STATISTICS")
print("="*70)

# Get cache statistics from lru_cache
cache_info = fib.cache_info()
print(f"\nCache info: {cache_info}")
print(f"  - hits: {cache_info.hits} (cached values used)")
print(f"  - misses: {cache_info.misses} (new calculations)")
print(f"  - currsize: {cache_info.currsize} (values currently cached)")
print(f"  - maxsize: {cache_info.maxsize} (maximum cache size)")

hit_rate = cache_info.hits / (cache_info.hits + cache_info.misses) * 100 if (cache_info.hits + cache_info.misses) > 0 else 0
print(f"\nCache efficiency: {hit_rate:.1f}% of calls used cached values!")

# ============================================================================
# MANUAL MEMOIZATION COMPARISON
# ============================================================================

print("\n" + "="*70)
print("COMPARISON: Manual Memoization vs @lru_cache")
print("="*70)

# Manual memoization approach
def manual_fib_with_cache():
    """Example of manual memoization (what @lru_cache does internally)."""
    cache = {}
    
    def fib_internal(n):
        if n in cache:
            return cache[n]
        
        if n < 2:
            result = n
        else:
            result = fib_internal(n - 1) + fib_internal(n - 2)
        
        cache[n] = result
        return result
    
    return fib_internal

manual_fib = manual_fib_with_cache()

print("""
Manual approach (complex, error-prone):
    def manual_fib(n):
        cache = {}
        if n in cache:
            return cache[n]
        # ... rest of logic

Using @lru_cache (simple, Pythonic):
    @lru_cache(maxsize=None)
    def fib(n):
        # ... regular recursive logic
        # Caching is handled automatically!

Advantages of @lru_cache:
    1. Clean, readable code
    2. No manual cache management
    3. Cache statistics available
    4. Cache can be cleared with cache_clear()
    5. Works with any function that has hashable arguments
""")
