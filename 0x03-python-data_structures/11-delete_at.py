#!/usr/bin/python3
def delete_at(my_list: list = [], idx: int = 0) -> list:
    if 0 <= idx < len(my_list):
        my_list[idx:idx+1] = []
    return my_list
