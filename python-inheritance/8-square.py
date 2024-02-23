#!/usr/bin/python3
""" this module contains subclass Square that inherits from subclass Rectange that inherits from class BaseGeometry """

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
        
        
    def area(self):
        """ area method returns width * height of the instance"""
        
        return self.__width * self.__height
        
        
    def __str__(self):
        """ returns a string representation of the rectangle instance """
        
        return "[Rectangle] {}/{}".format(self.__width, self.__height)    

            
class Square(Rectangle):
    """ defines a class Square that inherits from class Rectangle which inherits from class BaseGeometry """

    def __init__(self, size):
        """ 
        initializes an instance of the class Square
        
        Args:
        size: must be private and a positive integer
        """
        
        self.integer_validator("size", size)
        self.__size = size
        
        
    def area(self):
        """ area method returns size * size of the instance """
        
        return self.__size * self.__size   

print(issubclass(Square, Rectangle))