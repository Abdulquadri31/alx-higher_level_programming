#!/bin/bash
# A script to display all HTTP methods the server at a given URL accept.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
curl -sI -X OPTIONS "$URL" | grep -i "Allow:" | cut -d' ' -f2-
