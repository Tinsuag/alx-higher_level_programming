#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """writes and returns the ampunt of characters entered"""
    with open(filename, 2, mode='w', encoding='utf-8') as f:
        len = f.write(text)

    return len
