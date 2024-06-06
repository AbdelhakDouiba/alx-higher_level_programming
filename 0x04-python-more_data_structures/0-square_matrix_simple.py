#!/usr/bin/python3
def square_matrix_simple(matrix: list = []) -> list:
    new_matrix = []
    for row in matrix:
        new_matrix += [[i * i for i in row]]
    return new_matrix
