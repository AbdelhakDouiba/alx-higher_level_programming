#!/usr/bin/python3
"""
This is "2-append_write" Module
"""


def append_write(filename: str = "", text: str = "") -> int:
    """appends a string at the end of a text file (UTF8) and returns
       the number of characters added"""

    with open(filename, "a", encoding="UTF-8") as my_file:
        written_chars = my_file.write(text)
    return written_chars
