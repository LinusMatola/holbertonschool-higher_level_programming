#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square with size"""
    def __init__(self, size=0):
        """initializes the private attribute size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square's area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
