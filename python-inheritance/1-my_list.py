#!/usr/bin/python3
"""This module defines a custom list class."""


class MyList(list):
    """This class inherits from list and can print a sorted copy."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
