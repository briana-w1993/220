"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    number_of_words = 0
    for i in in_file.readlines():
        words = i.split()
        for j in words:
            number_of_words += 1
            out_file.write(str(number_of_words) + " " + j + "\n")




def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    employee_pay = 0
    for i in in_file.readlines():
        employee_info = i.split()
        first_n = employee_info[0]
        last_n = employee_info[1]
        pay_rate = float(employee_info[2])
        hours = float(employee_info[3])
        weeks_pay = (pay_rate + 1.65) * hours
        employee_stats = first_n + " " + last_n + " " + str(weeks_pay)
        out_file.write(str(employee_stats) + "\n")





def calc_check_sum(isbn):
    isbn_number = 0
    isbn.replace('-', "")
    counter = 10
    for i in range (len(isbn)):
        print(isbn[i])
        isbn_number += counter * int(isbn[i])
        counter -= 1
    return isbn_number





def send_message(file_name, friend_name):
    pass


def encode():
    pass


def send_safe_message(file_name, friend_name, key):
    pass


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
