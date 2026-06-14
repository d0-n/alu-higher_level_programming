#!/usr/bin/python3
"""This module defines a function that lists attributes of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
