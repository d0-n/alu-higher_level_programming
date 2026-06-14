#!/usr/bin/python3
"""This module provides a function to append text to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return number of added chars."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
