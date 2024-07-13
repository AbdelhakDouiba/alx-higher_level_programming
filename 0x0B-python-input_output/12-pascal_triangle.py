#!/usr/bin/python3
"""
This is "12-pascal_triangle" module
"""


def pascal_triangle(n: int) -> list:
    """returns a list of lists of integers representing the Pascal’s
       triangle of n"""

    if n <= 0:
        return []

    pascal = [[1] for i in range(n)]

    for i in range(1, n):
        j = 1

        while len(pascal[i]) < i + 1:
            if j < len(pascal[i-1]):
                pascal[i] += [pascal[i-1][j] + pascal[i-1][j-1]]
            else:
                pascal[i] += [1]
            j = j + 1
    return pascal
