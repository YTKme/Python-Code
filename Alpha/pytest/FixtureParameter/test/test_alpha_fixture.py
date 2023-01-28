"""
Test Alpha Fixture
~~~~~~~~~~~~~~~~~~
"""

import sys

import pytest

from Alpha.logging.GeneralLogger import logger


# Configure logger
test_alpha_fixture_logger = logger.Logger('test-alpha-fixture')
test_alpha_fixture_logger.setLevel(logger.DEBUG)


@pytest.mark.usefixtures('generate_number_list')
def test_alpha_fixture_add_success(generate_number_list):
    """
    """
    first_number_list = generate_number_list(size=5,
                                             max_size=sys.maxsize)
    second_number_list = generate_number_list(size=10,
                                              max_size=sys.maxsize)

    print(f'Type First: {type(first_number_list)}')

    for i, fn in enumerate(first_number_list):
        print(f'First Number List: {i}, {fn}')

    print(f'Type Second: {type(second_number_list)}')

    for i, sn in enumerate(second_number_list):
        print(f'Second Number List: {i}, {sn}')
