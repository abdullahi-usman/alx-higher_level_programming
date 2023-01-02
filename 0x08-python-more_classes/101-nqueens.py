#!/usr/bin/python3
"""Module of the type nqueens
Meant tp print the number of queens moves
on a chess board
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if type(sys.argv[1]) != int:
        print("N must be a number")
        sys.exit(1)

    num = int(sys.argv[1])

    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
