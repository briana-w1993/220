"""
Briana Addison
Homework 10
hw10.py

Problem: This code uses booleans and classes
I certify that this assignment is entirely my own work.
"""

def fibonacii(n):
    num = n
    if num < 1:
        return None
    else:
        fib_1 = num - 1
        fib_2 = num - 2
    return fib_1 + fib_2 - 1

def interest(principle, rate):
    while principle > 1:
        total = principle * (1 + rate)
        return total

def syracuse(n):
    number = []

    while n != 1:
        if n%2 == 0 :
            new = n/2
            number.append(new)
            return number
        else:
            new = 3 * (n + 1)
            number.append(new)
            return number

def goldbach(n):
    number = []
    while n >= 4:
        if n%2 == 0:
            prime = n%2
            result = prime + n
            number.append(result)
        else:
            return None


