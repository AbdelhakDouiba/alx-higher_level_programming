#!/usr/bin/python3

def islower(c: str) -> bool:
    '''
        islower - checks for lowercase character.
        @c: Single character string to check.
        Return: True if c is a lowercase letter, False otherwise.
    '''
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False
