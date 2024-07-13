#!/usr/bin/python3
'''
This is "0-read_file" Module
'''


def read_file(filename: str = ""):
    '''reads a text file (UTF8) and prints it to stdout'''

    with open(filename, encoding="UTF-8") as my_file:
        print(my_file.read(), end="")
