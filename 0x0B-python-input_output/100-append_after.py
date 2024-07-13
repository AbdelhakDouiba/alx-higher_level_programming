#!/usr/bin/python3
"""
This is "100-append_after" module
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
       containing a specific string"""

    with open(filename, "r+", encoding="UTF-8") as ff:
        content = ""

        for line in ff.readlines():
            content += line

            if search_string in line:
                content += new_string

        ff.write(content)
