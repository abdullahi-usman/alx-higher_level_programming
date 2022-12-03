#!/usr/bin/python


def new_in_list(my_list, idx, element):
    """Replace elements at index

    Args:
        my_list: the list
        idx: the index
        element: the element

    Returns:
        The new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list.copy()

    new_list[idx] = element

    return (new_list)
