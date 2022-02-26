"""
Name: Briana Addison
hw6.py

Problem: This program solves several problems using strings, ord, and chr

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""



import math


def cash_converter():
    integer = eval(input("enter an integer: "))
    integer = str(integer)
    cash = "That is {}{}{}".format("$", integer, ".00")
    print(cash)


def encode():
    message = input("enter a message")
    user_key = eval(input("enter a key"))
    for i in range(len(message)):
        translate_message = message[i]
        translate_message = ord(translate_message)
        shift = translate_message + user_key
        final_message = chr(shift)
        print(final_message, end="")


def sphere_area(radius):
    area = (4 * math.pi * (radius ** 2))
    return area


def sphere_volume(radius):
    volume = (4/3 * math.pi * (radius ** 3))
    return volume


def sum_n(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


def sum_n_cubes(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i ** 3
    return sum


def encode_better():
    phrase = input("Enter phrase")
    key = input("Enter key")
    for i in range(len(phrase)):
        character_val = ord(phrase[i]) - 65
        key_val = ord(key[i % len(key)]) - 65
        encode_val = ((character_val + key_val) % 57) + 64
        encode_text = chr(encode_val)
        print(encode_text, end="")


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
