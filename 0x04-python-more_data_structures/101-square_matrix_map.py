#!/usr/bin/python3
def square_matrix_map(matrix: list = []) -> list:
    return list(map(lambda x: list(map(lambda i: i * i, x)), matrix))
