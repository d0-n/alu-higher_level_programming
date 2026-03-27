#!/usr/bin/python3
"""Send a POST request with an email parameter using urllib and print the response body."""

import sys
import urllib.parse
import urllib.request


def main():
    """Send POST data containing the email and display response text."""
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
