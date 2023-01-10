#!/usr/bin/python3
'''
Has student information to print
and store some information
in a file
'''


class Student:
    '''
    Student, contains first_name, last_name
    and age of a student
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''
    convert the student to json
    and return the representation
    '''
    def to_json(self, attrs=None):
        json = vars(self)

        if attrs is not None:
            list = {}
            for item in json:
                if item in attrs:
                    list[item] = json[item]

            return list

        return json

    def reload_from_json(self, json):
        c_items = vars(self)
        for item in json:
            match item:
                case 'first_name':
                    self.first_name = json[item]
                    break

                case 'last_name':
                    self.last_name = json[item]
                    break

                case 'age':
                    self.age = json[item]
                    break
