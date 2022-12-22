#!/usr/bin/python3

""" Module Documetation
    This module demonstrates documentation as specified by
    the `Google Python Style Guide`_. Docstrings may extend
    over multiple lines. Sections are created with a section
    header and a colon followed by a block of indented text.
"""


class Square:
    """ Class Documentation
    This module demonstrates documentation as specified
    by the `Google Python Style Guide`_. Docstrings may extend
    over multiple lines. Sections are created with a section header
    and a colon followed by a block of indented text.
    """

    def __init__(self, size=0):
        """     Function Documentation
        This module demonstrates documentation as specified
        by the `Google Python Style Guide`_. Docstrings may extend
        over multiple lines. Sections are created with a section
        header and a colon followed by a block of indented text.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """     Function - Area Documentation
        This module demonstrates documentation as specified
        by the `Google Python Style Guide`_. Docstrings may extend
        over multiple lines. Sections are created with a section
        header and a colon followed by a block of indented text.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """     Function - Get Size
        This module demonstrates documentation as specified
        by the `Google Python Style Guide`_. Docstrings may extend
        over multiple lines. Sections are created with a section
        header and a colon followed by a block of indented text.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """     Function - Set Size
        This module demonstrates documentation as specified
        by the `Google Python Style Guide`_. Docstrings may extend
        over multiple lines. Sections are created with a section
        header and a colon followed by a block of indented text.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        if self.__size <= 0:
            print("--")

        for i in range(0, self.__size):
            print("#" * self.__size)
