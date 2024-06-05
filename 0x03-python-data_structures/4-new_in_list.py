#!/usr/bin/python3
def new_in_list(my_list: list, idx: int, element: int) -> list:
    if 0 <= idx < len(my_list):
        return my_list[:idx] + [element] + my_list[idx+1:]
    return my_list
