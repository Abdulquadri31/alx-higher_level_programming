#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
A peak is an element that is greater than or equal to its neighbors.
"""

def find_peak(list_of_integers):
    """
    Finds a peak element in the list.
    A peak element is greater than or equal to its neighbors.
    Args:
    list_of_integers (list): A list of integers.
    
    Returns:
    int: The peak element.
    """
    if not list_of_integers:
        return None

    def binary_search(low, high):
        mid = (low + high) // 2
        # Check if mid is a peak element
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        # If the left neighbor is greater, search in the left half
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search(low, mid - 1)
        # Otherwise, search in the right half
        else:
            return binary_search(mid + 1, high)

    return binary_search(0, len(list_of_integers) - 1)
