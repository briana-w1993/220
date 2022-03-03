import math

from graphics import Point


def distanve(p1, p2):
    result_a = math.pow(p2.getX() - p1.getX(), 2)
    result_b = math.pow(p2.getY() - p1.getY(), 2)
    #return math.sqrt
    return math.sqrt(result_a + result_b)

point_a = Point(2,3)
point_b = Point(3,5)

def sum_diff(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val, diff_val

my_sum, my_diff = sum_diff(10, 7)
print (my_sum)

def get_discount(price, sale):
    price = price * (1 - sale)
    print(price)

price = 100
get_discount(price, .20)
print(price)
