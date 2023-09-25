#!/usr/python3
def safe_print_list(mylist[], i):
    for element in mylist:
        if (element > i):
            break
        a = (mylist[element]) + (10 ** element)
        element += 1
    return (a)