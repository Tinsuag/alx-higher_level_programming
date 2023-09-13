#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        my_newlist = my_list[:]
        my_newlist[idx] = element
        return my_newlist
    