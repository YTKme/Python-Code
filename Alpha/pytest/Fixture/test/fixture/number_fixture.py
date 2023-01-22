"""
Test Fixture
~~~~~~~~~~~~
"""

import random
import sys

import pytest


RANDOM_SEED = random.randrange(sys.maxsize)
random.seed(RANDOM_SEED)

class NumberFixture:

    @pytest.fixture(scope='class', autouse=True)
    def generate_number_list(size: int = 10,
                             max: int = sys.maxsize) -> tuple[list, list]:
        """Generate Number List

        :param size: the size of the number list to generate, defaults to 10
        :type size: int, optional
        :return: the list of number(s)
        :rtype: generator, list
        """
        
        # Generate a list of random number(s)
        number_list = [random.randrange(max) for n in range(size)]

        yield number_list
