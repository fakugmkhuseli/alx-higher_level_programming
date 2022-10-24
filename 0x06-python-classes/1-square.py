#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a square."""

    __size = 0       # Private instance attribute

    def __init__(self, size):
        """Initialize attributes

        Args:
            self: The object itself
            size: The size of the square.
        """
        self.__size = size
