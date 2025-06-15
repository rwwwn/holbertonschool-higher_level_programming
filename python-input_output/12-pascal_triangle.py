#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n.

    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        prev_row = triangle[i - 1]
        # Calculate middle values based on previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
