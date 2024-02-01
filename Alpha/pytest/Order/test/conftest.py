"""Configure Test"""

from typing import Union

from pytest import Config
from pytest import ExitCode
from pytest import Session

from Core.logging.Logging import logger

# Configure Logger
conftest_logger = logger.Logger('conftest-logger')
conftest_logger.setLevel(logger.DEBUG)


def pytest_addoption(parser):
    """Register Command Line Option(s)

    :param parser: The parser for command line option(s)
    :type parser: pytest.Parser
    """
    conftest_logger.info('pytest Add Option')
    conftest_logger.debug(f'Parser: {parser}')


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info('pytest Configure')
    conftest_logger.debug(f'Config: {config}')


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the `Session` object has been created and before
    performing collection and entering the run test loop

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info('pytest Session Start')
    conftest_logger.debug(f'Session: {session}')


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]):
    """Finish Session

    :param session: The pytest session object
    :type session: pytest.Session
    :param exitstatus: The status which pytest will return to the system
    :type exitstatus: Union[int, pytest.ExitCode]
    """
    conftest_logger.info('pytest Session Finish')
    conftest_logger.debug(f'Session: {session}')
    conftest_logger.debug(f'Exit Status: {exitstatus}')


def pytest_unconfigure(config: Config):
    """Unconfigure Test

    Called before test process is exited

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info('pytest Unconfigure')
    conftest_logger.debug(f'Config: {config}')
