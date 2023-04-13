#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9rectangle').Rectangle


class Square(Rectangle):
    """Represent a new square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
        size (int) The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init = size