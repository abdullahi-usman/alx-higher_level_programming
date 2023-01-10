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
    def to_json(self):
        return vars(self)
