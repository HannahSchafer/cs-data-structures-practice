
def count_list_r(my_list):
    """Counts items in list recursively."""

    if len(count_list_r) < 1:
        return 0

    return count_list_r(my_list[1:]) + 1    


def reverse_list(lst):
    """Reverses a list. This list can have inner lists. Function should 
    reverse the inner lists as well."""

    new_list = lst[::-1]

    for i, item in enumerate(new_list):
        if isinstance(item, list):
            new_list[i] = reverse_list(item)

    return new_list


def sum_recursive(lst, i=0):
    """Recursively find the sum of numbers in a list"""

    if not lst:
        return 0

    return lst[i] + sum_recursive(lst, i + 1)