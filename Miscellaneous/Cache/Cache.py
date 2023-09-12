"""
Cache
~~~~~
"""

from functools import wraps


def memoize(func):
    """Simple memoization (cache) decorator.
    
    Note: The decorator is not thread safe.
    
    :param func: The function to be memoized (cached).
    :type func: function
    :return: The memoized (cached) function.
    :rtype: function
    """
    memo = {} # Cache

    # Decorator factory
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Memoized (cached) function."""
        # Create a unique key based on the function arguments
        key = str(args) + str(kwargs)

        # The `key` is not in cache (cache miss)
        if key not in memo:
            memo[key] = func(*args, **kwargs)
        
        # The `key` is in cache (cache hit)
        return memo[key]
    
    # Return the memoized (cached) function
    return wrapper