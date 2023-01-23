"""
Test Fixture
~~~~~~~~~~~~
"""

import random
import sys

import pytest


RANDOM_SEED = random.randrange(sys.maxsize)
random.seed(RANDOM_SEED)

@pytest.fixture
def generate_number_list(size: int = 10,
                         max_size: int = sys.maxsize) -> list:
    """Generate Number List

    :param size: the size of the number list to generate, defaults to 10
    :type size: int, optional
    :return: the list of number(s)
    :rtype: generator, list
    """

    def _generate_number_list(size, max_size):
    
        # Generate a list of random number(s)
        number_list = [random.randrange(max_size) for n in range(size)]

    yield _generate_number_list
