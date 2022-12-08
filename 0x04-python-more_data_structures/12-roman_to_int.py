#!/usr/bin/python3

def roman_to_int(roman_string):
    res = 0
    while roman_string != "":
        if "XIX" in roman_string:
            res = res + 19
            roman_string = roman_string.replace("XIX", "", 1)
        elif "IX" in roman_string:
            res = res + 9
            roman_string = roman_string.replace("IX", "", 1)
        elif "IV" in roman_string:
            res = res + 4
            roman_string = roman_string.replace("IV", "", 1)
        elif "XIV" in roman_string:
            res = res + 14
            roman_string = roman_string.replace("XIV", "", 1)
        elif "X" in roman_string:
            res = res + 10
            roman_string = roman_string.replace("X", "", 1)
        elif "I" in roman_string:
            res = res + 1
            roman_string = roman_string.replace("I", "", 1)
        elif "V" in roman_string:
            res = res + 5
            roman_string = roman_string.replace("V", "", 1)
        elif "L" in roman_string:
            res = res + 50
            roman_string = roman_string.replace("L", "", 1)
        elif "C" in roman_string:
            res = res + 100
            roman_string = roman_string.replace("C", "", 1)
        elif "D" in roman_string:
            res = res + 500
            roman_string = roman_string.replace("D", "", 1)
        elif "M" in roman_string:
            res = res + 1000
            roman_string = roman_string.replace("M", "", 1)

    return res;

roman_to_int("")