#!/usr/bin/python3
"""Defining a square printing function"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for row in range(size):
        for el in range(size):
            print("#", end="")
        print("")
