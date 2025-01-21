#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter."""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    
    request = Request(url, data)
    with urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
