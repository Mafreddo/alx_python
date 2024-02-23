#!/usr/bin/python3
""" this module contains subclass Rectange that inherits from class BaseGeometry """

class BaseGeometry:
    """ defines the class BaseGeometry """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate if the given value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """  
              
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ defines the subclass Rectangle inheritting from class BaseGeometry """

    def __init__(self, width, height):
        """ 
        initializes an instance of the class Rectange with width and height
        
        Args:
            width: must be private and a positive integer
            height: must be private an a positive integer
        
        check with integer_validator
        """
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height