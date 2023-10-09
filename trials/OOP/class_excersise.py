#!/usr/bin/python3
class Student:
    def __init__(self, name, color, height):
        self.__name = name
        self.__color = color
        self.__height = height
    
    """this will give the program a read access to the internal variables"""
    @property
    def name(self):
        return self.__name
    
    """this will give the access to write the given attributes of the instance"""
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Please enter the new name")
        else:
            self.__name = new_name
            print("Name change was successful. the student name is now " + self.__name)
            
student1 = Student("Tinsae", "black", 170)
print(student1.name)
"""changing the name of the student"""
student1.name = "Tesfamichael" 