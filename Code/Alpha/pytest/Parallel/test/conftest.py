"""
Test Configuration
~~~~~~~~~~~~~~~~~~

This module implement test configuration for testing application.
"""

import pytest

@pytest.fixture(scope='session', autouse=True)
def setup():
    print(f'Setup Fixture')
    yield


@pytest.fixture(scope='session', autouse=True)
def teardown():
    yield
    print(f'Teardown Fixture')
