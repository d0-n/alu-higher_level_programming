#!/usr/bin/python3
"""This module provides a function to get object dictionary for JSON."""


def class_to_json(obj):
    """Return the dictionary description of a simple object."""
    return obj.__dict__
