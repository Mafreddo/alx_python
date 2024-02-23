'''Creating our base class that will be refferenced through the entire project'''
class Base:

    '''Creating a static attribute which will hold the value 0'''
    __nb_objects = 0

    '''Creating new instances of our base'''
    def __init__(self, id =None):
        '''Check if the instance id is not set to none then return the value of the instance'''
        if id is not None:
            self.id = id
        else:
            '''If it is set to None then the static attribure will be implemented by 1'''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects