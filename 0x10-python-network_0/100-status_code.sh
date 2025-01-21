#!/bin/bash
# A script to send a request to a URL and display only the status code.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
curl -o /dev/null -s -w "%{http_code}" "$URL"
