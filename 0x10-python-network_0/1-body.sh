#!/bin/bash
# A script that takes a URL as input, sends a GET request

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

# Use curl to send a GET request and display body if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$URL" | grep -q "200" && curl -s "$URL"
