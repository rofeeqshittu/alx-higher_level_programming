#!/usr/bin/python3
""" Defines a pascal_triangle function """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's
    triangle of n """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element in each row is always 1

        # Calc the middle element of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
