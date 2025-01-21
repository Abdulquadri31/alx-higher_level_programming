#!/bin/bash
# A script that takes a URL as input, sends a GET request
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
