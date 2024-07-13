#!/usr/bin/python3
'''
This is "1-write_file" Module
'''


def write_file(filename: str = "", text: str = "") -> int:
    '''writes a string to a text file (UTF8) and returns
       the number of characters written'''

    with open(filename, "w", encoding="UTF-8") as ff:
        written = ff.write(text)
    return written
