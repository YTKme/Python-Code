"""
Test Parallel
~~~~~~~~~~~~~

This module implement test functionality for parallel test.
"""

from Code.Core.logging.Logging import logger


# Configure Logger
conftest_logger = logger.Logger('conftest-logger')
conftest_logger.setLevel(logger.DEBUG)

def test_a():
    print('Test A')