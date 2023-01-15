#!/usr/bin/python3
'''
Square module for the square
class and its properties
'''

from rectangle import Rectangle


class Square(Rectangle):
    '''
    This is the square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Init the constructor and call super method
        '''
        super().__init__(size, size, x, y)

    @property
    def size(self):
        '''
        Get the size
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''
        Set the size
        '''
        self.width = size
        self.height = size

    def __str__(self):
        '''
        Get a formatted string
        '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        '''
        Update the class with the
        appropriate methods properties
        '''
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError as ex:
                return
        else:
            for key, value in kwargs.items():
                match key:
                    case 'id':
                        self.id = value
                    case 'size':
                        self.size = value
                    case 'x':
                        self.x = value
                    case 'y':
                        self.y = value

    def to_dictionary(self):
        '''
        Convert everything to string
        '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
