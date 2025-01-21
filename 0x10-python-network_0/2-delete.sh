#!/bin/bash
# A script that sends a DELETE request to a URL

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

# Use curl to send a DELETE request and display the body of the response
curl -s -X DELETE "$URL"
