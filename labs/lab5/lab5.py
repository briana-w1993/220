"""
Name: Briana Addison
lab5.py

Problem: This program solves several problems using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *
from math import *
def triangle():
    win = GraphWin("Triangle", 700, 700)
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    user_triangle = Polygon(point1, point2, point3)
    user_triangle.setFill("pink")
    user_triangle.draw(win)
    side1_X = point2.getX() - point1.getX()
    side1_Y = point2.getY() - point1.getY()
    side2_X = point3.getX() - point2.getX()
    side2_Y = point3.getY() - point2.getY()
    side3_X = point1.getX() - point3.getX()
    side3_Y = point1.getY() - point3.getY()
    length1 = sqrt((side1_X ** 2) + (side1_Y ** 2))
    length2 = sqrt((side2_X ** 2) + (side2_Y ** 2))
    length3 = sqrt((side3_X ** 2) + (side3_Y ** 2))
    perimeter = length1 + length2 + length3
    s = (length1 + length2 + length3) / 2
    area = sqrt(s * (s - length1) * (s - length2) * (s - length3))
    perimeter_text = Text(Point(350, 600), "perimeter:" + str(perimeter))
    area_text = Text(Point(350, 625), "area: " + str(area))
    perimeter_text.draw(win)
    area_text.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text_entry = Entry(Point(200, 240), 5)
    red_text_entry.getText()

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text_entry = Entry(Point(200, 270), 5)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text_entry = Entry(Point(200,300), 5)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_text_entry.draw(win)
    green_text_entry.draw(win)
    blue_text_entry.draw(win)

    win.getMouse()





    for i in range(5):
        red_value = red_text_entry.getText()
        green_value = green_text_entry.getText()
        blue_value = blue_text_entry.getText()
        color = color_rgb(eval(red_value), eval(green_value), eval(blue_value))
        shape.setFill(color)
        win.getMouse()


    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Enter a string")
    first_char = user_string[0]
    print(first_char)
    last_char = user_string[-1]
    print(last_char)
    between_char = user_string[2:5]
    print(between_char)
    fir_last_char = user_string[0] + user_string[-1]
    print(fir_last_char)
    for i in range(10):
        first_three = user_string[0:3]
        print(first_three)
    for i in user_string:
        each_char = i
        print(each_char)
    length = len(user_string)
    print(length)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2] , values[0], eval(values[5])
    print(x)
    x = values[2] + values[0] + eval(values[5])
    print(x)
    x = len(values)
    print(x)



def another_series():
    num = eval(input("How many terms would you like"))
    print( end=" ")
    for i in range(num ):
        number = i % 3 * 2

        print((number + 2),end=" ")
    print("sum: ", 2* (i + num ) )




def target():
    win = GraphWin("Target", 700, 700)
    width = 300
    white_ring = Circle(Point(350, 350), width)
    black_ring = Circle(Point(350,350) ,width/2)
    blue_ring = Circle(Point(350,350),width/4)
    red_ring = Circle(Point(350,350),width / 6)
    yellow_ring = Circle(Point(350, 350), width / 8)
    white_ring.draw(win)
    white_ring.setFill("white")
    black_ring.draw(win)
    black_ring.setFill("black")
    blue_ring.draw(win)
    blue_ring.setFill("blue")
    red_ring.draw(win)
    red_ring.setFill("red")
    yellow_ring.draw(win)
    yellow_ring.setFill("yellow")


    message = Text(Point(600, 350),"Click to close")
    message.draw(win)
    win.getMouse()
    win.close()


