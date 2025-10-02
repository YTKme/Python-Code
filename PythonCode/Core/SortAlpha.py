"""
Sort Alpha
~~~~~~~~~~

The SortAlpha module provide example(s) to sort data structure(s).
"""


def sort_dictionary_by_key(data: dict, reverse: bool = False) -> dict:
    """Sort Dictionary By Key

    Sort a dictionary by its key(s) in the specified order.

    :param data: The dictionary to be sorted.
    :type data: dict
    :param reverse: Whether to sort in descending order, default to
        False (ascending order).
    :type reverse: bool

    :return: The sorted dictionary.
    :rtype: dict
    """

    return dict(sorted(
        data.items(),
        key=lambda item: item[0],
        reverse=reverse,
    ))


def sort_dictionary_by_value(data: dict, reverse: bool = False) -> dict:
    """Sort Dictionary By Value

    Sort a dictionary by its value(s) in the specified order.

    :param data: The dictionary to be sorted.
    :type data: dict
    :param reverse: Whether to sort in descending order, default to
        False (ascending order).
    :type reverse: bool

    :return: The sorted dictionary.
    :rtype: dict
    """

    return dict(sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=reverse,
    ))


def sort_list_dictionary_by_key(data: list, reverse: bool = False) -> list:
    """Sort List Dictionary By Key

    Sort a list of dictionary by a specified key in the specified order.

    :param data: The list of dictionary to be sorted.
    :type data: list
    :param reverse: Whether to sort in descending order, default to
        False (ascending order).
    :type reverse: bool

    :return: The sorted list of dictionary.
    :rtype: list
    """

    return sorted(
        data,
        key=lambda item: list(item.keys())[0],
        reverse=reverse,
    )


def sort_list_dictionary_by_value(
    data: list,
    key: str,
    reverse: bool = False
) -> list:
    """Sort List Dictionary By Value

    Sort a list of dictionary by a specified value in the specified order.

    :param data: The list of dictionary to be sorted.
    :type data: list
    :param key: The key to sort by.
    :type key: str
    :param reverse: Whether to sort in descending order, default to
        False (ascending order).
    :type reverse: bool

    :return: The sorted list of dictionary.
    :rtype: list
    """

    return sorted(
        data,
        key=lambda item: item[key],
        reverse=reverse,
    )
