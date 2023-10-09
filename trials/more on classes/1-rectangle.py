#!/usr/bin/python3
class Rectangle:
    def __init__(self,height, width):
        self.height = height
        self.width = width
        
    @property
    def height(self):
        return self.__height
    def width(self):
        return self.__width
    
    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width