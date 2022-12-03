#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    args_len = len(argv) - 1
    arg_name = "arguments"
    sep = ":"
    if args_len <= 1:
        arg_name = "argument"
        sep = "."

    print("{} {}{}".format(args_len, arg_name, sep))
    for arg_int in range(1, args_len + 1):
        print("{}: {}".format(arg_int, argv[arg_int]))
