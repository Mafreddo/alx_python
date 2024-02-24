#!/usr/bin/python3
"""_This module is for a class Square that inherits from Rectangle_

    Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    the area() method must be implemented
"""

class BaseGeometry:
    """This is class defines class BaseGeometry.
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """This is a class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

class Square(Rectangle):
    """This is a class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

    def __repr__(self):
        return f"Square({self._Rectangle__width})"
    