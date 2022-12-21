#!/usr/bin/python3

class Square:
    """ This module demonstrates documentation as specified by the `Google Python
    Style Guide`_. Docstrings may extend over multiple lines. Sections are created
    with a section header and a colon followed by a block of indented text.
    
    """
    __size = 0;
    def __init__(self, size = None) -> None:
        __size = size