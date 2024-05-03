"""
Test Thread Async IO
~~~~~~~~~~~~~~~~~~~~

The TestThreadAsyncIO module execute test(s) for the `ThreadAsyncIO`
module.
"""
import timeit

import pytest

from PythonCode.Concurrency import ThreadAsyncIO


def test_fetch_website_thread():
    """Test Fetch Website Thread"""

    # Execute
    start = timeit.default_timer()
    ThreadAsyncIO.fetch_website_thread()
    stop = timeit.default_timer()
    print(f'Test Fetch Website Thread Total: {stop - start}')
