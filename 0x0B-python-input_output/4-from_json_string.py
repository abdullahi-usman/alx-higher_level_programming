#!/usr/bin/python3
'''
This file has some functions that decode
the string pass as json
and return an object
'''

import json


def from_json_string(my_str):
    '''
    return the str as an
    object representation
    '''
    return json.loads(my_str)
