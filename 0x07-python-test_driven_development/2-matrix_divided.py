#!/usr/bin/python3
'''
This is matrix_divided Module
Defining matrix_divided function that divides all elements of a matrix.
'''


def matrix_divided(matrix: list, div) -> list:
    '''divides all elements of a matrix.
        Args:
            matrix: the target matrix
            div: the denominator

        Returns:
            a new matrix
    '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    my_matrix = []
    for i in matrix:
        row = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            row += [round(j / div, 2)]
        my_matrix += [row]
    return my_matrix
