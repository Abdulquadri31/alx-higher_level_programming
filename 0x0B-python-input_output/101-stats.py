#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys

def print_metrics(file_size, status_codes):
    """
    Prints the computed metrics.

    Args:
        file_size (int): Total size of files.
        status_codes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    """
    Main function to compute metrics from stdin.
    """
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count_lines = 0

    try:
        for line in sys.stdin:
            # Increment line count
            count_lines += 1
            
            # Split the line into components
            parts = line.split()
            if len(parts) < 7:
                continue

            # Add to file size
            try:
                size = int(parts[-1])
                file_size += size
            except ValueError:
                continue

            # Count the status code
            try:
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                continue

            # Print metrics every 10 lines
            if count_lines % 10 == 0:
                print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)

if __name__ == "__main__":
    main()
