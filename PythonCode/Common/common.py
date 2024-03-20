"""
Common
~~~~~~

The Common module.
"""

import random
import time


def fuzz(is_fuzz: bool = False) -> None:
    """Random Fuzz

    Fuzz(ing) is an automated software testing technique that involves
    providing invalid, unexpected, or random data as inputs to a
    computer program.

    Fuzz(ing) is also a technique for amplifying race condition errors
    to make them more visible.

    :param is_fuzz: Whether or not to enable fuzzing, defaults
        to `False`
    :type is_fuzz: bool
    """
    if is_fuzz:
        time.sleep(random.random())
