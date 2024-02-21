"""
Test Asynchronous Queue Gamma
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from PythonCode.Asynchronous.AsynchronousQueueGamma import AsynchronousQueueGamma


class TestAsynchronousQueueGamma():
    """Test Asynchronous Queue Gamma"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/1',
                'https://httpbin.org/anything/2',
                'https://httpbin.org/anything/3',
                'https://httpbin.org/anything/4',
                'https://httpbin.org/anything/5',
                'https://httpbin.org/anything/6',
                'https://httpbin.org/anything/7',
                'https://httpbin.org/anything/8',
                'https://httpbin.org/anything/9',
                'https://httpbin.org/anything/10',
                'https://httpbin.org/anything/11',
                'https://httpbin.org/anything/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        gamma = AsynchronousQueueGamma()

        await gamma.fetch_recursive(
            source_list=source_list,
        )
