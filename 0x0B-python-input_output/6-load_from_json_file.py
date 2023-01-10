#!/usr/bin/python3
'''
FIle contains functions that loads
string from file and loads the content
into a json object
'''

import json


def load_from_json_file(filename):
    '''
    load json from file and turns the
    content into an object
    '''
    with open(filename) as file:
        return json.loads(file.read())
