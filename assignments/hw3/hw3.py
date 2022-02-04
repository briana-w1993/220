"""
Name: Briana Addison
hw3.py

Problem: This program solves several problems using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def average():
    num_grades = eval(input("How many grades will you enter?"))
    grade_counter = 0
    for i in range (num_grades):
        grade_counter = grade_counter + eval(input("Enter grade:"))
    print("average is", (grade_counter/num_grades))


def tip_jar():
    tip_counter = 5
    num_tips = 0
    for i in range (tip_counter):
        num_tips = num_tips + eval(input("How much would you like to donate?"))
    print("total tips: ", num_tips)



def newton():
    root_num = eval(input("What number do you want to square root?"))
    approx = root_num
    times_approx = eval(input("How many time should we improve the "
                           "approximation?"))
    for i in range(times_approx):
        approx = (approx + (root_num/approx)) / 2
    print("The square root is approximately", approx)


def sequence():
    num_terms = eval(input("How many terms would you like?"))
    print(1, end=" ")
    for i in range(num_terms):
        num_terms = i+i%2+1
        print(num_terms, end=" ")



def pi():
    num_series = eval(input("How many terms in the series?"))
    numer = 0
    denom = 1
    pi_mult = 1
    for i in range(num_series):
        numer = numer + (i+1)%2 *2
        denom = denom + i % 2 * 2
        pi_mult = pi_mult * (numer/denom)
    pi_approx = pi_mult * 2
    print(pi_approx)


if __name__ == '__main__':
    pass
