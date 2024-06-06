#!/usr/bin/python3
def search_replace(my_list: list, search: int, replace: int) -> list:
    new_list = []
    new_list += [i if i != search else replace for i in my_list]
    return new_list
