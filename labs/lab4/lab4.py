"""
Briana Addison
Lab 4
lab4.py
Greeting Card
Problem: This code makes a Valentine's Day greeting card
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def greeting_card():
    win = GraphWin("Greeting Card", 800, 800)
    win.setBackground("pink")
    valentines = Text(Point(400,100), "Happy Valentines Day!")
    valentines_2 = Text(Point(400,200), "You shot my heart!")
    valentines.setSize(28)
    valentines_2.setSize(20)
    heart_bottom = Polygon(Point(400, 700), Point(190, 400), Point(610, 400))
    heart_left = Circle(Point(300, 375), 110)
    heart_right = Circle(Point(500, 375), 110)
    heart_bottom.setFill("crimson")
    heart_right.setFill("crimson")
    heart_left.setFill("crimson")
    heart_right.setOutline("crimson")
    heart_left.setOutline("crimson")
    heart_bottom.setOutline("crimson")
    heart_right.draw(win)
    heart_left.draw(win)
    heart_bottom.draw(win)
    valentines.setFill("crimson")
    valentines_2.setFill("crimson")
    valentines.draw(win)
    valentines_2.draw(win)
    arrow_stick = Line(Point(100,200), Point(300, 400))
    arrow_head = Polygon(Point(300,400), Point(300,430), Point(350, 430))
    arrow_head.setFill("black")
    arrow_stick.setFill("black")
    arrow_stick.setWidth(5)
    arrow_head.draw(win)
    arrow_stick.draw(win)
    for i in range(15):
        arrow_stick.move(10,10)
        arrow_head.move(10,10)
        time.sleep(0.5)
    message = Text(Point(400,750), "Click to close")
    message.draw(win)
    win.getMouse()
    win.close()

