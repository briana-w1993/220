import math
from math import *

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        number = self.radius
        return number

    def surface_area(self):
        rad = self.get_radius()
        area = 4 * math.pi * rad ** 2
        return area

    def volume(self):
        rad = self.get_radius()
        volume = 4/3 * math.pi * rad ** 3
        return volume

