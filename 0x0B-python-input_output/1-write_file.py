#!/usr/bin/python3
"""
this program writes a string into a second document
"""


def write_file(filename="", text=""):
    """this will write"""
    with open(filename, mode='w', encoding="utf-8") as f:
        len = f.write(text)

    return len
