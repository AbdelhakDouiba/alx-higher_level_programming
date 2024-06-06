#!/usr/bin/python3
def square_matrix_simple(matrix: list = []) -> list:
    new_matrix = []
    for row in matrix:
        new_matrix += [(lambda x: [i * 2 for i in x])(row)]
    return new_matrix
