"""
Briana Addison
Lab 10
lab10.py

Problem: This code makes a door and a button
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from button import Button
from door import Door
from graphics import *

def main():
    win = GraphWin("Test", 700, 700)
    win.setBackground("white")
    button = Button(Rectangle(Point(200,50), Point(400,250)),"exit")
    door = Door(Rectangle(Point(200, 300),Point(400, 600)), "closed")
    door.draw(win)
    door.color_door("pink")
    door.get_label().draw(win)
    button.get_label().draw(win)
    button.draw(win)

    win.getMouse()

    win.getMouse()

    if door.is_clicked(Point(win.mouseX,win.mouseY)):
        door.draw(win)
        door.color_door("purple")


    win.getMouse()
    win.close()





