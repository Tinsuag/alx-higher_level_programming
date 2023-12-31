#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, new_size):
        if new_size == "":
            print("Enter a number")
        else:
            self.__size = new_size

    def area(self):
            return self.__size ** 2
        