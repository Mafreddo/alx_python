#!/usr/bin/python3
"""Public instance method: def integer_validator(self, name, value): 
    that validates value

    Raises:
        Exception(name): _is always a string_
        TypeError(if value is not an integer): _message <name> must be an integer_
        ValueError(if value is less or equal to 0): _message <name> must be greater than 0_
"""

class BaseGeometry:
    """This is class defines class BaseGeometry.
    """
    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """Validate the value as an integer greater than 0."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
             


# bg = BaseGeometry()

# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", 89)

# try:
#     bg.integer_validator("name", "John")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("age", 0)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("distance", -4)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))