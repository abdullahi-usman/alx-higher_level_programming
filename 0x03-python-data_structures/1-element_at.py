#!/usr/bin/python3

def element_at(my_list, idx):
    """Print elements at index

    Args:
        my_list: the list
        idx: the index

    Returns:
        None
    """
    
    if idx < 0 or idx >= len(my_list):
        return None
    
    return my_list[idx]
