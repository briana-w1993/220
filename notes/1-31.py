import graphics


point_a = graphics.Point(50, 70)
point_b = graphics.Point(90, 100)
print(point_a.getX(), point_a.getY())
point_a.move(10, 0)
print(point_a.getX(), point_a.getY())

win = graphics.GraphWin("CSCI 220", 700, 700)
point_a.draw(win)
middle =  graphics.Point(350,  350)
middle.draw(win)

my_circle = graphics.Circle(middle, 70)
my_circle.draw(win)

input("hit enter to exit")
