#!/usr/bin/python3
"""Fetch and display the ALU intranet status page response details using requests."""

import requests


def main():
    """Send a GET request and print response body details."""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
