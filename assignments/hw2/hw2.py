"""
Name: Briana Addison
hw2.py

Problem: This code solves the problem of several mathmatical equations

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound "))
    sum = 1
    for i in range(upper_bound):
        sum = upper_bound * 3
    print(sum)


def multiplication_table():
    for i in range(1,11):
        for k in range(1,11):
            print(i * k ,end = "\t")
        print()



def triangle_area():
    a = eval(input("Enter side a length:"))
    b = eval(input("Enter side b length:"))
    c = eval(input("Enter side c length:"))
    s = (a + b + c)/2
    final = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(final)


def sum_squares():

    lower_range = eval(input("Enter lower range:"))
    upper_range = eval(input("Enter upper range:"))
    sum = 0
    for i in range(lower_range, (upper_range+1)):
        sum = sum + (i * i)
    print(sum)

def power():
    base = eval(input("Enter base"))
    exponent = eval(input("Enter exponent"))
    final = base
    for i in range(exponent - 1 ):
        final = final * base
    print(base,"^",exponent, "=", final )


if __name__ == '__main__':
    pass
