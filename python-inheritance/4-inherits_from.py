#!/usr/bin/python3
"""This module checks whether an object inherits from a specific class."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not exactly it."""
    return isinstance(obj, a_class) and type(obj) is not a_class
