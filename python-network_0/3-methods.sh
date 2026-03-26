#!/bin/bash
# Display all HTTP methods the server will accept using OPTIONS
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d" " -f2-
