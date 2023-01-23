"""
Test Alpha Fixture
~~~~~~~~~~~~~~~~~~
"""

import sys

import pytest


@pytest.mark.usefixtures('generate_number_list')
def test_alpha_fixture_add_success(generate_number_list):
    """
    """
    first_number_list = generate_number_list(size=5,
                                             max_size=sys.maxsize)
    second_number_list = generate_number_list(size=10,
                                              max_size=sys.maxsize)
