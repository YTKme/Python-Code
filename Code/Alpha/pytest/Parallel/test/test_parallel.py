"""
Test Parallel
~~~~~~~~~~~~~

This module implement test functionality for parallel test.
"""

import time

import pytest


@pytest.mark.parametrize('case', range(10))
def test_alpha(case):
    print(f'Test Alpha...{case}')
    time.sleep(3)
