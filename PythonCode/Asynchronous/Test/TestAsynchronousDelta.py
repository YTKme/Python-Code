"""
Test Asynchronous Queue Delta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from PythonCode.Asynchronous.AsynchronousDelta import AsynchronousDelta


class TestAsynchronousDelta:
    """Test Asynchronous Delta"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/Delta/1',
                'https://httpbin.org/anything/Delta/2',
                'https://httpbin.org/anything/Delta/3',
                'https://httpbin.org/anything/Delta/4',
                'https://httpbin.org/anything/Delta/5',
                'https://httpbin.org/anything/Delta/6',
                'https://httpbin.org/anything/Delta/7',
                'https://httpbin.org/anything/Delta/8',
                'https://httpbin.org/anything/Delta/9',
                'https://httpbin.org/anything/Delta/10',
                'https://httpbin.org/anything/Delta/11',
                'https://httpbin.org/anything/Delta/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        delta = AsynchronousDelta()

        await delta.fetch_recursive(
            source_list=source_list,
        )
