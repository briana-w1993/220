"""
Briana Addison
Lab 12
lab12.py

Problem: This code uses while loops to make algorithms.
I certify that this assignment is entirely my own work.
"""
from random import randint

def find_and_remove_first(list, value):
    i = 0
    while value != list[i]:
       list.pop(i).replace("Briana")

def read_data(file_name):
    data = []
    file = open(file_name, "r")
    line = file.readline()
    while line:
        data_info = line.split()
        i = 0
        while i < len(data_info):
            data_return = eval(data_info[i])
            data.append(data_return)
            i += 1
        line = file.readline()
    return data

def is_in_linear(search_val, values):
    i = 0
    while values:

        if search_val == values[i]:
            return True
        else:
            return False
    i += 1

def good_input():

    user_number = eval(input("Enter a number between 1-10: "))
    while user_number > 10 or user_number < 1:
        if user_number > 10:
            user_number = eval(input("Your number is too high! Enter a number "
                               "between 1-10: "))
        elif user_number < 1:
            user_number = eval(input("Your number is too low! Enter a number "
            "between 1-10: "))
        else:
            return user_number
    return user_number

def num_digits():
    user_number = eval(input("Enter a positive integer: "))
    divide_counter = 0
    while user_number:
        if user_number == 0 or user_number < 0:
            return None
        while user_number != 0:
            user_number = user_number // 10
            divide_counter += 1
        print(divide_counter)

def hi_lo_game():
    game_counter = 1
    rand_num = randint(1, 100)
    user_guess = eval(input("Guess a number between 1 and 100:"))
    while game_counter < 7:
        if user_guess < rand_num:
            user_guess = eval(input("Your guess is too low :( guess again!"))
            game_counter += 1
        elif user_guess > rand_num:
            user_guess = eval(input("Your guess is too high :( guess again!"))
            game_counter += 1

    if user_guess == rand_num:
        print("You win in", game_counter, "guesses!")
    elif game_counter == 7:
        print("sorry, you lose :(. The number was",rand_num)

