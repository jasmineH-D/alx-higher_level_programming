#!/usr/bin/python3
"""Defining new class Square"""
class Square:
     """class Square
     Attributes:
        __size (int): size of square
        __position (tuple): position of square in 2df space
     """

     def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def size(self):
         """gets value of size"""
         return self.__size
    @property
    def position(self):
         return self.__position
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        return (self.__size * self.__size)
    def my_print(self):
        if self.__size == 0:
             print()
             return
         for i in range(0, self.__position[1]):
             print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for z in range(self.__size)]))
