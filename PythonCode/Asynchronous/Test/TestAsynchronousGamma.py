"""
Test Asynchronous Gamma
~~~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from PythonCode.Asynchronous.AsynchronousGamma import AsynchronousGamma


class TestAsynchronousGamma:
    """Test Asynchronous Gamma"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/Gamma/1',
                'https://httpbin.org/anything/Gamma/2',
                'https://httpbin.org/anything/Gamma/3',
                'https://httpbin.org/anything/Gamma/4',
                'https://httpbin.org/anything/Gamma/5',
                'https://httpbin.org/anything/Gamma/6',
                'https://httpbin.org/anything/Gamma/7',
                'https://httpbin.org/anything/Gamma/8',
                'https://httpbin.org/anything/Gamma/9',
                'https://httpbin.org/anything/Gamma/10',
                'https://httpbin.org/anything/Gamma/11',
                'https://httpbin.org/anything/Gamma/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        gamma = AsynchronousGamma()

        await gamma.fetch_recursive(
            source_list=source_list,
        )
