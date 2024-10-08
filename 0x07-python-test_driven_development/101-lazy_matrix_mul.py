#!/usr/bin/python3
"""Module for matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module

    Args:
        m_a: The first matrix as a list of lists of integers/floats
        m_b: The second matrix as a list of lists of integers/floats

    Returns:
        A new matrix representing the result of the multiplication
    """
    return np.matmul(m_a, m_b)
