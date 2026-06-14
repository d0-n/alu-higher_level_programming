#!/usr/bin/python3
"""This module defines a Square class that can print itself."""


class Square:
    """This class defines a square by size."""

    def __init__(self, size=0):
        """Initialize a square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
