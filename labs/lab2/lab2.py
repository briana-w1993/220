"""
Briana Addison
Lab 2
Calculations
Problem: This code solves the problem of calculating means
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
def means() :
    amount_of_values = eval(input("enter the valuse to be entered"))
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1


    for i in range(amount_of_values):
        number = eval(input("enter value"))
        rms_average = rms_average + number ** 2
        harmonic_mean = harmonic_mean + 1 / number
        geometric_mean = geometric_mean * number

    rms_average = math.sqrt((rms_average)/amount_of_values)
    harmonic_mean = amount_of_values/ harmonic_mean
    geometric_mean = geometric_mean ** (1/amount_of_values)
    print("This number is the root mean square.", round(rms_average, 3))
    print("This number is the harmonic mean.", harmonic_mean)
    print("This number is the geometric mean." , round(geometric_mean,3))
