#!/usr/bin/python3
"""This module defines a Student class with JSON reload support."""


class Student:
    """This class represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if type(attrs) is list and all(type(a) is str for a in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all student attributes using key/value in json dict."""
        for key, value in json.items():
            setattr(self, key, value)
