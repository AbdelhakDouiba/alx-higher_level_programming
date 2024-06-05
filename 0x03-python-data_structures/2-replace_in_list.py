#!/usr/bin/python3
def replace_in_list(my_list: list, idx: int, element: int) -> list:
    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return my_list
    return None
