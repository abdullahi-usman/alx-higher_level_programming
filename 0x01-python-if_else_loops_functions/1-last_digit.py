#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = str(number)
last_num = number[len(number) - 1]
word = "0"

if int(number) < 0:
    last_num = str(-int(last_num))

if int(last_num) > 5:
    word = "greater than 5"
elif int(last_num) < 6 and int(last_num) != 0:
    word = "less than 6 and not 0"


print(f"Last digit of {number} is {last_num} and is {word}")