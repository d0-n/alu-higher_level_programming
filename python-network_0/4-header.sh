#!/bin/bash
# Send a GET request with custom X-HolbertonSchool-User-Id header
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
