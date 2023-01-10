#!/usr/bin/python3
'''
COntains functions to loads
and update the list of a file
and then to write it back
'''

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == '__main__':
    list = []
    filename = 'add_item.json'
    try:
        list = load_from_json_file(filename)
    except Exception as e:
        pass

    list = list + sys.argv[1:]

    save_to_json_file(list, filename)
