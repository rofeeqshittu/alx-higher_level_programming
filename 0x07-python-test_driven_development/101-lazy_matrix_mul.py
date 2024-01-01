#!/usr/bin/python3
"""
    Contains a lazy_matrix_mul() func that multiplies 2 matrix using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Calculates 2 matrix using the Numpy module """

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    try:
        result = np.matmul(np_a, np_b)
        return result
    except ValueError as e:
        raise ValueError(str(e))
