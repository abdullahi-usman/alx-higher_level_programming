#!/usr/bin/python3

'''
Base module class for
creating other modules

'''

import json


class Base:
    '''
    Base clas for both
    the rectangle and square
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        static method to convert object
        to json string
        '''
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        static method to convert this
        string to python object
        '''
        if json_string is None or len(json_string) <= 0:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        This method saves the object to
        a file
        '''
        list = []
        for obj in list_objs:
            list.append(cls.to_dictionary(obj))

        with open(f"{cls.__name__}.json", "w+", encoding='utf-8') as file:
            file.write(Base.to_json_string(list))

    @classmethod
    def create(cls, **dictionary):
        '''
        this a contructor method
        capable of creating other object from
        their class
        '''
        clazz = cls(1, 1)
        clazz.update(**dictionary)

        return clazz

    @classmethod
    def load_from_file(cls):
        '''
        Loads this class information from its
        appropriate .json file
        '''
        instances = []
        try:
            with open(f"{cls.__name__}.json", 'r', encoding='utf-8') as file:
                for ins in Base.from_json_string(file.read()):
                    instances.append(cls.create(**ins))

                return instances
        except FileNotFoundError:
            return []
