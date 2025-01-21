#!/bin/bash
# A script to display all HTTP methods the server at a given URL accept.
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
