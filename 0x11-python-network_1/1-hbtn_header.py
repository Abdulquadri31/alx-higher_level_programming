#!/usr/bin/python3
"""Fetches the X-Request-Id header from a given URL."""

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
