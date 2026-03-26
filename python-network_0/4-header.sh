#!/bin/bash
# Send a GET request with custom X-HolbertonSchool-User-Id header
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
