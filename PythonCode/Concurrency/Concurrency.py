"""
Concurrency
~~~~~~~~~~~
"""

import random
import threading
import time


_FUZZ = True


def fuzz():
    """Random Fuzz

    Fuzz(ing) is an automated software testing technique that involves
    providing invalid, unexpected, or random data as inputs to a
    computer program.

    Fuzz(ing) is also a technique for amplifying race condition errors
    to make them more visible.
    """
    if _FUZZ:
        time.sleep(random.random())
