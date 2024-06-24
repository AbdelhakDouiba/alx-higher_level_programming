#!/usr/bin/python3
'''
This is "100-matrix_mul" module
matrix_mul - multiplies 2 matrices
'''


def matrix_mul(m_a: list, m_b: list) -> list:
    '''multiplies 2 matrices'''
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    for i in m_a:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_t = [[0 for a in range(len(m_b[0]))] for a in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b)):
            for k in range(len(m_b)):
                m_t[i][j] = m_t[i][j] + m_a[i][k] * m_b[k][j]
    return m_t
