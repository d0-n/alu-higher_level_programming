#!/usr/bin/python3
"""Send a POST request with an email parameter using requests and print the response body."""

import sys
import requests


def main():
    """Send POST data containing the email and display response text."""
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)


if __name__ == "__main__":
    main()
