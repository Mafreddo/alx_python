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

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

        """
        Initializes a new Square instance.

        Parameters:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        
        type(size) == int
        if type(size) != int:
            raise TypeError("size must be an integer") 
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
# Public instance method: def area(self): that returns the current square area
 
    def area(self):
        """Calculates area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
#  Access and update private attribute
 
    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        """
        
        
        type(value) == int
        """
        Initializes a new Square instance.

        Parameters:
            value (int): The value of the size. 

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer") 
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


    def my_print(self):
        """
        Prints the square using the character #.
        
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# my_square = Square(3)
# my_square.my_print()

# Square(5).my_print()