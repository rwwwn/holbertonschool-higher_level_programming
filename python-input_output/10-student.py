#!/usr/bin/python3
"""Module that defines the Student class with filtering."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                return {key: getattr(self, key) for key in attrs if
                        hasattr(self, key)}
        return self.__dict__
