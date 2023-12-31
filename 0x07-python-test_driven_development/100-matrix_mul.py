#!/usr/bin/python3
"""
    Module contains only a matrix_mul() that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Multiply 2 matrices """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if (m_a == []) or (m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == []) or (m_b == [[]]):
        raise ValueError("m_b can't be empty")

    # Validates the elements in each row
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

    # Validates the elements in each row of m_b
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Validates if matrix is rectangle
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compactibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication operation
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row_result.append(value)
        result.append(row_result)

    return result
