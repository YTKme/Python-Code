"""Argument Parser Module

This module implements different usage of argument parser.
"""

import argparse


def parse_argument():
    """Parse Argument

    :returns: the namespace with the parsed arguments
    :rtype: namespace
    """

    DESCRIPTION = (
        'Simple module to test the different usage of argument parser.'
        )
    
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    # Input
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        action='store', # Store the value
        dest='input', # Destination to store
        required=True,
        help='The `input` argument.'
    )

    return parser.parse_args()
