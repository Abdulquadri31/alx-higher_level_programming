#!/bin/bash
# A script to send a GET request with a custom header

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
curl -s -H "X-School-User-Id: 98" "$URL"
