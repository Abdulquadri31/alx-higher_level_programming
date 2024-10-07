#!/usr/bin/python3
"""N Queens Problem Solver."""
import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_not_integer(value):
    """Checks if the value is not an integer.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if value cannot be converted to an integer, False otherwise.
    """
    try:
        int(value)
    except ValueError:
        return True
    return False


def nqueens(n, row=0, queens=[]):
    """Solves the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard and number of queens.
        row (int): The current row to place a queen.
        queens (list): The list of queens' positions.

    Returns:
        list: A list of valid queen positions.
    """
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            nqueens(n, row + 1, queens + [[row, col]])


def is_safe(queens, row, col):
    """Checks if a queen can be placed at the given position.

    Args:
        queens (list): The list of queens' positions.
        row (int): The current row to check.
        col (int): The column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for q_row, q_col in queens:
        if q_col == col or \
           abs(q_row - row) == abs(q_col - col):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n_value = sys.argv[1]

    if is_not_integer(n_value):
        print("N must be a number")
        sys.exit(1)

    n = int(n_value)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
