#!/usr/bin/python3
"""This module defines a Square class with custom string output."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square with validated size."""

    def __init__(self, size):
        """Initialize square size after validation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string description of the square."""
        return "[Square] {0}/{0}".format(self.__size)
