"""
Briana Addison
Lab 10
button.py

Problem: This code makes a button
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        label_text = self.text
        return label_text

    def set_label(self, label):
        label.setText()

    def draw(self, win):
        self.shape.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        door_x_1 = self.shape.getP1().getX()
        door_x_2 = self.shape.getP2().getX()
        door_y_1 = self.shape.getP1().getY()
        door_y_2 = self.shape.getP2().getY()
        point_x = point.getX()
        point_y = point.getY()
        if door_x_1 <= point_x <= door_x_2 and door_y_1 <= point_y <= door_y_2:
            return True
        else:
            return False


    def color_button(self, color):
        self.shape.color.setFill(color)
