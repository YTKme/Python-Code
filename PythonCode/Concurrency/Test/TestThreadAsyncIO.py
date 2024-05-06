"""
Test Thread Async IO
~~~~~~~~~~~~~~~~~~~~

The TestThreadAsyncIO module execute test(s) for the `ThreadAsyncIO`
module.
"""
import timeit

import pytest

from PythonCode.Concurrency import ThreadAsyncIO


@pytest.mark.asyncio
async def test_fetch_website_async():
    """Test Fetch Website Async"""

    # Execute
    start = timeit.default_timer()
    await ThreadAsyncIO.fetch_website_async()
    stop = timeit.default_timer()
    print(f'Test Fetch Website Async Total: {stop - start}')


def test_fetch_website_thread():
    """Test Fetch Website Thread"""

    # Execute
    start = timeit.default_timer()
    ThreadAsyncIO.fetch_website_thread()
    stop = timeit.default_timer()
    print(f'Test Fetch Website Thread Total: {stop - start}')
