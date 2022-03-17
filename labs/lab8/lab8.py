import math
from random import randint
from graphics import *

def get_random(move_amount):
    return randint(-move_amount, move_amount)

def did_collide(circle_ball1, circle_ball2):
    circle_ball1_X = circle_ball1.getCenter(circle_ball1.getP1())
    circle_ball2_X = circle_ball2.getCenter(circle_ball2.getP1())
    circle_ball1_Y = circle_ball1.getCenter(circle_ball1.getP2())
    circle_ball2_Y = circle_ball2.getCenter(circle_ball2.getP2())
    x_sqrt = (circle_ball2_X - circle_ball1_X) ** 2
    y_sqrt = (circle_ball2_Y - circle_ball1_Y) ** 2
    distance = math.sqrt(x_sqrt + y_sqrt)
    radius_sum =circle_ball1.getRaduis() + circle_ball2.getRadius()
    if radius_sum  > distance:
        return False
    else:
        return True

def hit_vertical(circle_ball, win):
    circle_ball_rad = circle_ball.getRadius()
    circle_ball_Y = circle_ball.getP2()
    screen_width = win.getWidth()
    if circle_ball_rad == screen_width or circle_ball_Y == screen_width:
        return True
    else:
        return False

def hit_horizontal(circle_ball, win):
    circle_ball_rad = circle_ball.getRadius()
    circle_ball_X = circle_ball.getP1()
    screen_height = win.getHeight()
    if circle_ball_rad == screen_height or circle_ball_X == screen_height:
        return True
    else:
        return False


def get_random_color():
     return color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))

def bumper():
    win = GraphWin("Bumper Cars", 800, 800)
    win.setBackground("white")



    circle_1 = Circle(Point(randint(0, 800), randint(0, 800)), 80)
    circle_2 = Circle(Point(randint(0, 800), randint(0, 800)), 80)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)
    for i in range(100):
        circle_1.move(get_random(100),get_random(100))
        circle_2.move(get_random(100),get_random(100))
        time.sleep(0.5)

    if did_collide(circle_1, circle_2) == True:
        circle_1.move(0,100)
        circle_2.move(0, 0)

    if hit_horizontal(circle_1 or circle_2, GraphWin) == True:
        circle_1.move(0,100)
        circle_2.move(0, 0)

    if hit_vertical(circle_1 or circle_2, GraphWin) == True:
        circle_1.move(0,100)
        circle_2.move(0, 0)


    win.getMouse()
    win.close()

