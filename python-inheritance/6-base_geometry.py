#!/usr/bin/python3
"""This module defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """This class represents a base geometry type."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
