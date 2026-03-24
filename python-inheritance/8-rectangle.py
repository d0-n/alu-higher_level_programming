#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle with validated dimensions."""

    def __init__(self, width, height):
        """Initialize rectangle width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
