"""
Name: Briana Addison
lab7.py

Problem: This program grades a classes test by calculating their weight and
average

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def weighted_average(in_file_name, out_file_name):
    input_file = open(in_file_name, "r")
    output_file = open(out_file_name, "w")
    student_info = input_file.readlines()


    for i in student_info:
        weights = 0
        averages = 0
        grades = 0

        student_info = i.split(":")
        student_grades = student_info[1].strip().split()
        for j in range(0, len(student_grades), 2):


            weights += eval(student_grades[j])
            grades = eval(student_grades[j + 1])
            averages = (weights * grades)
            averages = averages + j
            averages = averages/100
            if weights < 100:
                averages = " Weight is less than 100!"

            if weights > 100:
                averages = " Weight is more than 100!"


        output_file.write(str(student_info[0]) +  str("'s average:") + str(
            averages) + "\n")

    input_file.close()
    output_file.close()
