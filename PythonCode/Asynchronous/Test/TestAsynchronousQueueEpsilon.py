"""
Test Asynchronous Queue Epsilon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from PythonCode.Asynchronous.AsynchronousQueueEpsilon import AsynchronousQueueEpsilon


class TestAsynchronousQueueEpsilon:
    """Test Asynchronous Queue Epsilon"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/Epsilon/1',
                'https://httpbin.org/anything/Epsilon/2',
                'https://httpbin.org/anything/Epsilon/3',
                'https://httpbin.org/anything/Epsilon/4',
                'https://httpbin.org/anything/Epsilon/5',
                'https://httpbin.org/anything/Epsilon/6',
                'https://httpbin.org/anything/Epsilon/7',
                'https://httpbin.org/anything/Epsilon/8',
                'https://httpbin.org/anything/Epsilon/9',
                'https://httpbin.org/anything/Epsilon/10',
                'https://httpbin.org/anything/Epsilon/11',
                'https://httpbin.org/anything/Epsilon/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        epsilon = AsynchronousQueueEpsilon()

        await epsilon.fetch_recursive(
            source_list=source_list,
        )
