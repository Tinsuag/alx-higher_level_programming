#!/usr/bin/python3
"""
this program reads a file
"""


def read_file(filename=""):
    """opening the file in secure way"""
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line, end="")
