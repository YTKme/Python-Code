"""
Alpha Fixture
~~~~~~~~~~~~~
"""

from pathlib import Path


def hello():
    """Hello Function

    The function provide general information on the current module.
    """

    current_file = Path(__file__).resolve()

    return f'Hello From Alpha Fixture Module: {current_file.name}'


def addition(first_number: int, second_number: int) -> int:
    """Add Two Number

    :param first_number: the first number to add
    :type first_number: int
    :param second_number: the second number to add
    :type second_number: int
    :return: the result of adding the first number to the second number
    :rtype: int
    """

    result = first_number + second_number
    
    return result


def subtraction(first_number: int, second_number: int) -> int:
    """Subtract Two Number

    :param first_number: the first number to subtract
    :type first_number: int
    :param second_number: the second number to get subtracted
    :type second_number: int
    :return: the result of subtracting the first number to the second
        number
    :rtype: int
    """

    result = first_number - second_number
    
    return result
