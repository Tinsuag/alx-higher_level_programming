#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
"""


def to_json_string(my_obj):
    """turns the string into a json equvalent no"""
    import json
    return json.dumps(my_obj)
