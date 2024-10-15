#!/usr/bin/python3
"""
Generates Pascal's triangle up to n levels.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle.

    Args:
        n (int): The number of levels of the triangle.

    Returns:
        list: A list of lists containing integers representing Pascal's triangle,
              or an empty list if n <= 0.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)  # Initialize a row with 1s
        if i > 1:  # Update the row with sums of the previous row's elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
