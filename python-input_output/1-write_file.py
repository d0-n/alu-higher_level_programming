#!/usr/bin/python3
"""This module provides a function to write text to a file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return number of written chars."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
