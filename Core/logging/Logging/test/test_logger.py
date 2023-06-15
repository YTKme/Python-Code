"""Test Logger

This module test functionality for the logger.
"""

import logging

from Core.logging.Logging import logger


def test_initialize_success():
    """Test a successful initialize of the logger class

    Create an instance of Logger and check to make sure the object
    is of Logger type.
    """

    test_logger = logger.Logger('test-logger')
    assert isinstance(test_logger, logger.Logger)


def test_initialize_failure():
    """Test a failure initialize of the logger class

    Create an instance of logging.Logger and check to see if the
    object is of Logger type.
    """

    test_logger = logging.Logger('test-logger')
    assert not isinstance(test_logger, logger.Logger)


def test_color_success():
    """Test a successful display of log messages and color

    Create an instance of Logger and log messages using different
    level to display different color.
    """

    test_logger = logger.Logger('test-logger')

    test_logger.debug('Debug Message')
    test_logger.info('Info Message')
    test_logger.warning('Warning Message')
    test_logger.error('Error Message')
    test_logger.critical('Critical Message')
