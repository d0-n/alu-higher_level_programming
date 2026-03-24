#!/usr/bin/python3
"""This module provides a function to serialize an object to JSON."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
