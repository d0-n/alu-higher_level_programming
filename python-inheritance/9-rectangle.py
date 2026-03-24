#!/usr/bin/python3
"""This module defines a full Rectangle class that inherits BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle with area and string output."""

    def __init__(self, width, height):
        """Initialize rectangle width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
