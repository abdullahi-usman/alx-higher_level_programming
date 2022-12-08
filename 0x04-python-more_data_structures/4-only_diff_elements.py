#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    uncommon_ls = []

    for mem in set_1:
        if mem not in set_2:
            uncommon_ls.append(mem)

    for mem in set_2:
        if mem not in set_1:
            uncommon_ls.append(mem)

    return (uncommon_ls)
