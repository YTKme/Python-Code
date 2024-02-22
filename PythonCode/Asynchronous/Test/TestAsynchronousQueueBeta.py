"""
Test Asynchronous Queue Beta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from PythonCode.Asynchronous.AsynchronousQueueBeta import AsynchronousQueueBeta


class TestAsynchronousQueueBeta():
    """Test Asynchronous Queue Beta"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/Beta/1',
                'https://httpbin.org/anything/Beta/2',
                'https://httpbin.org/anything/Beta/3',
                'https://httpbin.org/anything/Beta/4',
                'https://httpbin.org/anything/Beta/5',
                'https://httpbin.org/anything/Beta/6',
                'https://httpbin.org/anything/Beta/7',
                'https://httpbin.org/anything/Beta/8',
                'https://httpbin.org/anything/Beta/9',
                'https://httpbin.org/anything/Beta/10',
                'https://httpbin.org/anything/Beta/11',
                'https://httpbin.org/anything/Beta/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        beta = AsynchronousQueueBeta()

        await beta.fetch_recursive(
            source_list=source_list,
        )
