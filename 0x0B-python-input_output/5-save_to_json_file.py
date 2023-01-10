#!/usr/bin/python3
'''
Save JSON string to a file function
this functions can convert json obj to
string to save them
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Open filename or create it if not existed
    and write to the file, then return
    number written
    '''
    with open(filename, mode='w+') as file:
        file.write(json.dumps(my_obj))
