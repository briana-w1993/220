from graphics import Point, \
    Entry
import graphics

win = graphics.GraphWin('Face', 700, 700)

user_input = Entry(Point(5,5),30)
user_input.setText("Enter your name")
name = user_input.getText()
user_input.draw(win)
win.getMouse()
print(name)