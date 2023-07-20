"""
IIFE
~~~~

IIFE (Immediate Invoked Function Express)
"""

# Decorator to call function immediately
@lambda _: _()
def func() -> str:
    """Example function
    
    Cannot use the function again, but can use it as a variable
    """
    print('func() was called!')
    # The return is assigned to the function name
    return 'some value'

print(func)


# > python IIFE.py
# func() was called!
# some value