"""
Cache Alpha
~~~~~~~~~~~
"""
import time

from Cache import memoize


def fibonacci(n) -> int:
    """Return the `n` th Fibonacci number."""
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

@memoize
def fibonacci_memoization(n) -> int:
    """Return the `n` th Fibonacci number."""
    if n < 2:
        return n
    else:
        return fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    

def main():
    """The main function."""
    print(f'Fibonacci Without Memoization')
    tic = time.perf_counter()
    print(fibonacci(35))
    toc = time.perf_counter()
    print(f'Time Without Memoization: {toc - tic:0.4f} seconds')

    print(f'Fibonacci With Memoization')
    tic = time.perf_counter()
    print(fibonacci_memoization(50))
    toc = time.perf_counter()
    print(f'Time With Memoization: {toc - tic:0.4f} seconds')


if __name__ == '__main__':
    main()