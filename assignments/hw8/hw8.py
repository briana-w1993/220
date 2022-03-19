"""
Name: Briana Addison
<hw8>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke
"""
import math
from graphics import *

def add_ten(nums):
    for i in range (len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i]) ** 2



def sum_list(nums):
    list = 0
    for i in range(len(nums)):
        list += nums[i]
    return list


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])




def sum_of_squares(nums):
    list_num = []

    for i in range(len(nums)):
        split_num = nums[i].split(", ")
        to_numbers(split_num)
        square_each(split_num)
        list_num.append(sum_list(split_num))
    return list_num




def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year%4 == 0 :
        if year%100 == 0:
            if year%400 == 0:
                return True
            return False
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center_one = win.getMouse()
    center_two = win.getMouse()
    circumference_point_one = win.getMouse()
    circumference_point_two = win.getMouse()

    radius = math.sqrt(
        (center_one.getX() - circumference_point_one.getX()) ** 2 + (
                center_one.getY() - circumference_point_one.getY()) ** 2)
    circle_one = Circle(center_one, radius)
    circle_one.setFill("pink")
    circle_one.draw(win)
    circle_two = Circle(center_two, radius)
    circle_two.setFill("purple")
    circle_two.draw(win)
    if did_overlap(circle_one.getRadius(), circle_two.getRadius()) == True:
        touching = Text(Point(300, 450), "The circles are touching")
        touching.draw(win)

    else:
        not_touching = Text(Point(300, 450), "The circles are not touching")
        not_touching.draw(win)


    win.getMouse()
    win.close()


def did_overlap(circle_one:Circle, circle_two:Circle):
    distance = math.sqrt((circle_two.getCenter().getX() -
                         circle_one.getCenter().getX)) ** 2 + ((
        circle_two.getCenter().getY() - circle_one.getCenter().getY()) ** 2)
    if distance <= circle_one.getRadius() + circle_two.getRadius():
        return True
    else:
        return False



if __name__ == '__main__':
    pass
