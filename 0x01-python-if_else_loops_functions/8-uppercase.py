#!/usr/bin/python3

def uppercase(str: str):
    """
        uppercase - prints a string in uppercase followed by a new line.
        @str: the target string
    """
    var = ''
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            var += chr(ord(str[i]) - ord('a') + ord('A'))
        else:
            var += str[i]
    print('{}'.format(var))
