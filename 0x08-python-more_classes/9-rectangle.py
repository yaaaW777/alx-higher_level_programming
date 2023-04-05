#!/usr/bin/python3
"""Defining class of a rectangle"""


class Rectangle:
    """"Initializing the class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Args:
               Width: with of the rectangle
               height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """"width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns parametre of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width)*2

    def __str__(self):
        """returns a string with a special character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rect_str = ''
        for m in range(self.__height):
            for n in range(self.__width):
                try:
                    rect_str += str(self.print_symbol)
                except Exception:
                    rect_str += type(self).print_symbol
            if m < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message about a deleted object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggers rect or rect_1 if both are equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)