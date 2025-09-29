"""
Test Sort Alpha Class
~~~~~~~~~~~~~~~~~~~~~
"""


import pytest

from PythonCode.Core.SortAlpha import sort_dictionary_by_key
from PythonCode.Core.SortAlpha import sort_dictionary_by_value


class TestSortAlpha:
    """Test Sort Alpha Class"""

    @pytest.mark.parametrize("data, reverse, expected", [
        (
            {"Toyota": 3, "Honda": 1, "Ford": 4, "BMW": 2},
            False,
            {"BMW": 2, "Ford": 4, "Honda": 1, "Toyota": 3},
        ),
        (
            {"Banana": 5, "Apple": 2, "Orange": 8, "Grapes": 3},
            False,
            {"Apple": 2, "Banana": 5, "Grapes": 3, "Orange": 8},
        ),
        (
            {"Zebra": 7, "Elephant": 4, "Lion": 6, "Tiger": 5},
            True,
            {"Zebra": 7, "Lion": 6, "Tiger": 5, "Elephant": 4},
        ),
    ])
    def test_sort_dictionary_by_key(self, data, reverse, expected):
        """Test Sort Dictionary By Key"""

        data = sort_dictionary_by_key(data, reverse=reverse)

        assert data == expected


    @pytest.mark.parametrize("data, reverse, expected", [
        (
            {"Toyota": 3, "Honda": 1, "Ford": 4, "BMW": 2},
            False,
            {"Honda": 1, "BMW": 2, "Toyota": 3, "Ford": 4},
        ),
        (
            {"Banana": 5, "Apple": 2, "Orange": 8, "Grapes": 3},
            False,
            {"Apple": 2, "Grapes": 3, "Banana": 5, "Orange": 8},
        ),
        (
            {"Zebra": 7, "Elephant": 4, "Lion": 6, "Tiger": 5},
            True,
            {"Zebra": 7, "Lion": 6, "Tiger": 5, "Elephant": 4},
        ),
    ])
    def test_sort_dictionary_by_value(self, data, reverse, expected):
        """Test Sort Dictionary By Value"""

        data = sort_dictionary_by_value(data, reverse=reverse)

        assert data == expected
