"""
Name: Briana Addison
<hw7>.py

Problem: This code solves the problem of using files in functions
Certification of Authenticity:
I certify that this assignment is entirely my own work.
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
    file_name = open(file_name, "r")
    friend_name = open(friend_name, "w")
    message = file_name.readlines()
    friend_name.write(message)





def send_safe_message(file_name, friend_name, key):
    from encryption import encode
    file_name = open(file_name,"r")
    friend_name = open(friend_name,"w")
    safe_encode = open("encryption.py", "r")
    file_name = file_name.readlines()
    safe_encode = safe_encode.readlines()
    message = encode(file_name, key)
    friend_name.write(str(message))




def send_uncrackable_message(file_name, friend_name, pad_file_name):
    from encryption import encode_better
    file_name = open(file_name, "r")
    friend_name = open(friend_name, "w")
    pad_file = open(pad_file_name, "r")
    file_name = file_name.readlines()
    pad_file = pad_file.readlines()
    message = encode_better(file_name, pad_file)
    friend_name.write(str(message))



if __name__ == '__main__':
    pass
