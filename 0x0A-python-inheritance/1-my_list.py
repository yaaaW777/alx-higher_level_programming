#!/usr/bin/python3
"""Defines an inherited list class Mylist."""


class Mylist(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
