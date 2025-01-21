#!/usr/bin/python3
"""Uses GitHub API with Basic Authentication to display user ID."""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get("id"))
    else:
        print(None)
