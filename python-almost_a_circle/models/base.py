""" This module contains the class Base """
class Base:
    """private class attribute for class Base, _nb_objects"""
    __nb_objects = 0
    
    # class constructor
    def __init__(self, id=None):
        """
        initializes an instance of class Base 
        
        Variables"
        __nb_objects = 0
        
        Args:
        id = None
        
        """
        # public instance attribute
        if id != None:
            self.id = id
        else:
            # increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects