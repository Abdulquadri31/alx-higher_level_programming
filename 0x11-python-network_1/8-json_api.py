#!/usr/bin/python3
"""Sends a POST request with a letter and handles the response."""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response['id']}] {json_response['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
