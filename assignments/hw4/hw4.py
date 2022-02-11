"""
Name: Briana Addison
hw4.py

Problem: This program makes several shapes using the graphics function.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

import math
from graphics import *
from math import *


def squares():
    win = GraphWin('Squares', 700, 700)
    init_square = Rectangle(Point(100, 100), Point(150, 150))
    init_square.setFill("pink")
    init_square.draw(win)
    first_message = Text(Point(350, 50), "Click to draw squares")
    first_message.draw(win)

    for i in range(5):
        user_click = win.getMouse()
        p1 = Point(user_click.getX() + 25, user_click.getY() + 25)
        p2 = Point(user_click.getX() - 25, user_click.getY() - 25)
        user_square = Rectangle(p2, p1)
        user_square.setFill("pink")
        user_square.draw(win)
    final_message = Text(Point(350, 600), "Click again to close")
    final_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    user_click = win.getMouse()
    user_click_2 = win.getMouse()
    user_rectangle = Rectangle(user_click, user_click_2)
    user_rectangle.setFill("light blue")
    user_rectangle.draw(win)
    length = user_click_2.getX() - user_click.getX()
    width = user_click_2.getY() - user_click.getY()
    perimeter = 2 * abs((length + width))
    area = abs(length * width)
    peri_message = Text(Point(250, 380), "Perimeter: " + str(perimeter))
    area = Text(Point(250, 400), "Area: " + str(area))
    peri_message.draw(win)
    area.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 500, 500)
    user_center = win.getMouse()
    user_circum = win.getMouse()
    user_radius = sqrt(((user_center.getX() - user_circum.getX()) ** 2) + (
        user_center.getY() - user_circum.getY()) ** 2)
    user_circle = Circle(user_center, user_radius)
    user_circle.setFill("plum")
    user_circle.draw(win)
    radi_message = Text(Point(250, 450), "Radius: " + str(user_radius))
    radi_message.draw(win)
    close_message = Text(Point(250, 50), "Click again to close")
    close_message.draw(win)
    win.getMouse()
    win.close()


def pi2():
    num_of_terms = eval(input("enter the number of terms to sum:"))
    total = 0
    num_add = int(num_of_terms/2) + (num_of_terms % 2)
    num_sub = int(num_of_terms/2)
    num = 4
    for i in range(num_add):
        denom = (4 * i) + 1
        frac = num/denom
        total = total + frac
    for i in range(num_sub):
        denom = (4 * i) + 3
        frac = num / denom
        total = total - frac

    print("pi approximation:", total)
    approx = abs(math.pi - total)
    print("accuracy:", approx)
