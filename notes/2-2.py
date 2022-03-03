from graphics import Point, \
    GraphWin, \
    Circle, \
    Text
import math

win = GraphWin('Face', 700, 700)
face = Circle(Point(350, 100), 100)
name = Text(Point(350, 600),"Briana")
name.draw(win)

left_eye = Circle(Point(325, 70), 25)
right_eye = left_eye.clone()
right_eye.move(50, 0)



left_eye.setFill('pink')
left_eye.setOutline('purple')
left_eye.setWidth(3)





face.draw(win)
right_eye.draw(win)
left_eye.draw(win)

input('enter to close')