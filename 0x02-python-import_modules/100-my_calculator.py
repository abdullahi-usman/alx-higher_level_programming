#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2][0]

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = 0

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        result = mul(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
