## Returning the size of a square

class Square():
    def __init__(self, size):
        self.__size = size
             
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)