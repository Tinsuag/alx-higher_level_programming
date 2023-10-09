#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            i = 0
            for n in position:
                if not isinstance(n,integer) && n > 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
                i++
            if(i != 2):
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                size.__position = position

    @property
    def size(self):
        return self.__size
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if value == "":
            print("Enter a number")
        else:
            self.__size = value
    def position(self, value):
        if value == "":
            print("Enter a number")
        else:
            self.___position = value

    """def area(self):
            return self.__size ** 2"""
    def my_print(self):
        i = 0
        if(self.__size == 0):
            print("")
        else:
            while(i < self.__size):
                print("#" * self.__size)
                i += 1
