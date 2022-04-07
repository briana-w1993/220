"""
Briana Addison
Lab 10
door.py

Problem: This code makes a door
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Door:
    def __init__(self,
                 shape,
                 label):
        self.shape = shape
        self.text = Text(
            shape.getCenter(),
            label)
        self.secret = False

    def get_label(self):
        label_text = self.text
        return label_text

    def set_label(self,
                  label):
        label.setText()

    def draw(self,
             win):
        self.shape.draw(
            win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self,
                   point):
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

    def open(self,
             color,
             label):
        self.shape.setFill(
            color)
        self.set_label(
            label)

    def close(self,
              color,
              label):
        self.shape.setFill(
            color)
        self.set_label(
            label)

    def color_door(self,
                   color):
        self.shape.setFill(
            color)

    def is_secret(self):
        if self.secret == True:
            return True
        else:
            return False

    def set_secret(self,
                   secret):
        self.secret = secret
