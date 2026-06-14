#!/usr/bin/python3
"""This module provides a function to save an object as JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
