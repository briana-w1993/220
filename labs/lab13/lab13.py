from labs.lab12 import algorithms
from graphics import *

def star_find(filename):
    file = open(filename, "r")
    file_info = file.readline()
    file_info = file_info.split()

    neutron_count = 0
    neutron_list = []


    for i in range(len(file_info)):
        star_numbers = eval(file_info[i])

        if star_numbers >= 4000 and star_numbers <= 5000:
            neutron_count = neutron_count + 1
            neutron_list.append(star_numbers)
            if neutron_count == 5:
                break
    if neutron_count == 5:
        print("you found 5 signals!")
        print("neutron count:", neutron_count)
        print("neutron list:", neutron_list)
        #
        file.close()
    else:
        print("you found", neutron_count, "signals!")
        print("neutron count:",neutron_count)
        print("neutron list:",neutron_list)
        file.close()



def selection_sort(values):
    numbers = values

    for i in range(len(numbers)):
        while numbers[i + 1] > numbers[i + 2]:
            unsort_value = numbers[0]
            numbers.sort()
            min = numbers[0]
            numbers.remove(min)
            numbers[0].append(unsort_value)


def calc_area(rect):
    width = rect.getP1().getX() + rect.getP1().getY()
    height = rect.getP2().getX() + rect.getP2().getY()
    area = width * height
    return area

def rect_sort(rectangles):
    for i in range(len(rectangles)):
        rectangles.sort()

        for j in range(len(rectangles)):
            calc_area(rectangles[j])











