#!/usr/bin/python3

"""This is a text indentation module
it is suppose to indent with two new line
after each dot or question mark (?) or (:)
so we are going to make it so. and dont forget to
check for type error
"""


def text_indentation(text=""):

    """This function indent the text and print
    it print text and append two new lines
    at the end of the string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    cur_index = 0
    last_word = ""
    INFINITY = 9999999999
    while True:
        cur_index = min(text.find(".") + 1 or INFINITY,
                        text.find("?") + 1 or INFINITY,
                        text.find(":") + 1 or INFINITY)

        if (cur_index == INFINITY):
            break

        last_word = text[0:cur_index + 1]
        print(last_word.strip(), end="\n\n")
        text = text[len(last_word):]

    if text != "":
        print(text.strip())
