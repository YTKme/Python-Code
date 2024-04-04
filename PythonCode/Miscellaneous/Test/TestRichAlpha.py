"""
Test Rich Alpha
~~~~~~~~~~~~~~~
"""


import pytest

from PythonCode.Miscellaneous.RichAlpha import RichAlpha


class TestRichAlpha:
    """Test Rich Alpha Class"""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'source_list', [
            [
                'https://httpbin.org/anything/Alpha/1',
                'https://httpbin.org/anything/Alpha/2',
                'https://httpbin.org/anything/Alpha/3',
                'https://httpbin.org/anything/Alpha/4',
                'https://httpbin.org/anything/Alpha/5',
                'https://httpbin.org/anything/Alpha/6',
                'https://httpbin.org/anything/Alpha/7',
                'https://httpbin.org/anything/Alpha/8',
                'https://httpbin.org/anything/Alpha/9',
                'https://httpbin.org/anything/Alpha/10',
                'https://httpbin.org/anything/Alpha/11',
                'https://httpbin.org/anything/Alpha/12',
            ],
        ]
    )
    async def test_fetch_recursive(
        self,
        source_list: list[str],
    ):
        """Test Fetch Recursive"""
        alpha = RichAlpha()

        await alpha.fetch_recursive(
            source_list=source_list,
        )
