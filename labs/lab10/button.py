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
        if point <= self.shape:
            return True
        else:
            return False


    def color_button(self, color):
        self.shape.color.setFill(color)
