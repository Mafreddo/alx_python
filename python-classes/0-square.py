# class Square:
#     """
#     A class that defines a square.

#     Attributes:
#         __size (int): The size of the square.

#     Methods:
#         __init__(self, size): Initializes a new Square instance with the given size.
#     """
    
#     def __init__(self, size):
#         self.__size = size

#     def get_size(self):
#         return self.__size

# # mysquare = Square(3) print(type(mysquare)) print(mysquare.dict_)
    
# mysquare = Square(3)
# print(type(mysquare))
# print(mysquare.__dict__)


#!/usr/bin/python3

# class Square:
#     """
#     A class that defines a square.

#     Attributes:
#         __size (int): The size of the square.

#     Methods:
#         __init__(self, size): Initializes a new Square instance with the given size.
#     """

#     def __init__(self, size):
#         """
#         Initializes a new Square instance.

#         Parameters:
#             size (int): The size of the square.
#         """
#         self.__size = size

# Example:
# my_square = Square(3)
# print(type(my_square))
# print(my_square.__dict__)


"""
This module defines a Square class.

The Square class represents a square geometric shape and has a private
instance attribute for the size.

Example:
    square = Square(5)
    print(square.get_area())  # Output: 25
"""

class Square:
    """This class defines a Square.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size