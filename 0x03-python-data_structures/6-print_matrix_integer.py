#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{}".format(num), end="")
        print()