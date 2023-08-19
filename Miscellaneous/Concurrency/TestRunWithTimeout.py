"""
Test Run With Timeout
~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

from .RunWithTimeout import run_with_timeout


@pytest.mark.parametrize(
    'command, duration',
    [
        ('ping 8.8.8.8', 5),
        ]
    )
def test_run_with_timeout(command, duration):
    """
    """
    process = run_with_timeout(
        command=command,
        timeout=duration,
        )