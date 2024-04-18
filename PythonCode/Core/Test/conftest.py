"""
Configure Test
~~~~~~~~~~~~~~

The Configure Test (`conftest`) module.
"""

import json
from pathlib import Path
from typing import Union

from pytest import (
    Config,
    ExitCode,
    Metafunc,
    Parser,
    PytestPluginManager,
    Session,
)
import tealogger


tealogger.set_level(tealogger.DEBUG)


"""
Initialization Hook
~~~~~~~~~~~~~~~~~~~
"""


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    """Register Command Line Option(s)

    Register argparse style options and ini style config values, called
    once at the beginning of a test run.

    :param parser: The parser for command line option(s)
    :type parser: pytest.Parser
    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    tealogger.info('pytest Add Option')
    tealogger.debug(f'Parser: {parser}')
    tealogger.debug(f'Plugin Manager: {pluginmanager}')


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration

    :param config: The pytest config object
    :type config: pytest.Config
    """
    tealogger.info('pytest Configure')
    tealogger.debug(f'Config: {config}')


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the `Session` object has been created and before
    performing collection and entering the run test loop

    :param session: The pytest session object
    :type session: pytest.Session
    """
    tealogger.info('pytest Session Start')
    tealogger.debug(f'Session: {session}')


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]):
    """Finish Session

    Called after whole test run finished, right before returning the
    exit status to the system.

    :param session: The pytest session object
    :type session: pytest.Session
    :param exitstatus: The status which pytest will return to the system
    :type exitstatus: Union[int, pytest.ExitCode]
    """
    tealogger.info('pytest Session Finish')
    tealogger.debug(f'Session: {session}')
    tealogger.debug(f'Exit Status: {exitstatus}')


def pytest_unconfigure(config: Config):
    """Unconfigure Test

    Called before test process is exited

    :param config: The pytest config object
    :type config: pytest.Config
    """
    tealogger.info('pytest Unconfigure')
    tealogger.debug(f'Config: {config}')


"""
Collection Hook
~~~~~~~~~~~~~~~
"""


def pytest_generate_tests(metafunc: Metafunc):
    """Generate Test Hook

    Generate (multiple) parametrized calls to a test function.
    Dynamically parametrize test(s) using test data from a JSON
    (JavaScript Object Notation) file. The data will align with the
    class and function name of the test(s).

    :param metafunc: Objects passed to the pytest_generate_tests hook
    :type metafunc: pytest.Metafunc
    """
    tealogger.info('pytest Generate Test')

    # Load the test data
    with open(Path(__file__).parent / 'DataAlpha.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    tealogger.debug(f'Meta Function: {metafunc}')
    tealogger.debug(f'Module Name: {metafunc.module.__name__}')
