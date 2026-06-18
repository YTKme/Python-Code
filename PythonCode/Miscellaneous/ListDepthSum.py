"""
List Depth Sum
~~~~~~~~~~~~~~

The ListDepthSum module implement the function(s) to calculate the sum
of integer(s), multiply by the depth, in a nested list.
"""

def list_depth_sum_recursive(integer_list: list, depth: int = 1) -> int:
    """
    List Depth Sum Resursive

    :param integer_list: The list of integer(s) and or (nested) list(s)
    :type integer_list: list
    :param depth: The current depth of the list, defaults to 1
    :type depth: int, optional
    """

    total_sum = 0

    for item in integer_list:
        if isinstance(item, list):
            total_sum += list_depth_sum_recursive(item, depth + 1)
        else:
            total_sum += item * depth

    return total_sum
