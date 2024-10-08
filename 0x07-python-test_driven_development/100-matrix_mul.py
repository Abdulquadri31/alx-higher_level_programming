#!/usr/bin/python3
"""
Module for matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix which is the product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists,
                   or if the elements in the matrices are not integers/floats,
                   or if rows in m_a or m_b are not of the same size.
        ValueError: If m_a or m_b are empty, or if they cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if len({len(row) for row in m_a}) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len({len(row) for row in m_b}) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            product_sum = sum(row[i] * m_b[i][col] for i in range(len(m_b)))
            new_row.append(product_sum)
        result_matrix.append(new_row)

    return result_matrix
