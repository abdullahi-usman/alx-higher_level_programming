#!/usr/bin/python3
'''
Rectnagle module that holds the
rectangle class
'''

from models.base import Base

class Rectangle(Base):
    '''
    Rectangle class derived from the base class
    conbining class and methods
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor: init all properties
        and class super constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Get the width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        Set the width
        '''
        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise TypeError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        '''
        Get the height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        Set the height
        '''
        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise TypeError('height must be > 0')

        self.__height = height

    @property
    def x(self):
        '''
        Get the x property
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        Set x property
        '''
        self.__x = x

    @property
    def y(self):
        '''
        Get y property
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        Set y property
        '''
        self.__y = y

    def area(self):
        '''
        Get the area
        '''
        return self.width * self.height

    def display(self):
        '''
        Dispaly the property of
        both x and y with width
        and height
        '''
        if (self.y > 0):
            for i in range(self.y):
                print('')

        for i in range(self.height):
            print(f"{' ' * self.x}{'#' * self.width}")

    def __str__(self):
        '''
        Get the string property
        '''
        return f"""[Rectangle] ({self.id}) {self.x}/{self.y}
                - {self.width}/{self.height}"""

    def update(self, *args, **kwargs):
        '''
        Update the string and property
        '''
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError as ex:
                return
        else:
            for key, value in kwargs.items():
                match key:
                    case 'id':
                        self.id = value
                    case 'width':
                        self.width = value
                    case 'height':
                        self.height = value
                    case 'x':
                        self.x = value
                    case 'y':
                        self.y = value

    def to_dictionary(self):
        '''
        convert everything to dictionary
        '''
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
