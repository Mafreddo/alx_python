# models/rectangle.py

""" This module contains the class Square """

from models.rectangle import Rectangle
""" imports class Rectangle into the module """
  
        
class Square(Rectangle):
    """ defines a class Square as a subclass of class Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes an instance of class Square """
        
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ string representation of the square """
        
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """ getter method for size """
        
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size """
        
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of the square """
        
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)