#!/usr/bin/python3
"""
    Module containing matrix_divided function that divides a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    if not all(
            isinstance(row, list) and
            all(isinstance(element, (int, float)) for element in row)
            for row in matrix):
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    result_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
    ]

    return result_matrix
