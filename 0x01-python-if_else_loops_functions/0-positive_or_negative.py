#!/usr/bin/python3
import random
number = random.randint(-10, 10)

word = "negative" if number < 0 else "positive"

if number == 0:
    word = "zero"

print("{} is {}".format(number, ))
