#!/usr/bin/python3
'''
This file has some function that
will transform some python
object to JSON
'''

import json


def to_json_string(my_obj):
    '''
    return my_obj as JSON
    if it permits else raise or return
    null
    '''
    return json.dumps(my_obj)
