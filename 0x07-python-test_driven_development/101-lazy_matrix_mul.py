#!/usr/bin/python3
'''
This is "101-lazy_matrix_mul" Module
lazy_matrix_mul - multiplies 2 matrices by using the module NumPy
'''


import numpy


def lazy_matrix_mul(m_a: list, m_b: list) -> list:
    '''multiplies 2 matrices by using the module NumPy

        Args:
            m_a: first matrice
            m_b: second matrice
    '''
    return numpy.dot(m_a, m_b)
