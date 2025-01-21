#!/bin/bash
# A script to send a POST request with JSON data from a file and display the response body.

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON file>"
    exit 1
fi

URL=$1
JSON_FILE=$2

# Check if the file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "File not found!"
    exit 1
fi

# Send the POST request with the contents of the JSON file
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL")

# Check if the response is a valid JSON
if echo "$response" | jq empty >/dev/null 2>&1; then
    echo "$response"
else
    echo "Not a valid JSON"
fi
