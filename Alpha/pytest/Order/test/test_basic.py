"""Test Basic"""

from Core.logging.Logging import logger

# Configure Logger
test_basic_logger = logger.Logger('test-basic-logger')
test_basic_logger.setLevel(logger.DEBUG)

def test_basic():
    """Test Basic"""
    test_basic_logger.info('Test Basic')
