#!/usr/bin/python3

def remove_char_at(str: str, n: int) -> str:
    '''
        remove_char_at - creates a copy of the string, removing the character
                         at the position n.
        Return: a copy of the string.
    '''
    str_copy = ''
    for i in range(len(str)):
        if i != n:
            str_copy += str[i]
    return str_copy
