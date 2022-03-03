import graphics
from graphics import Point, GraphicWin, Circle, Text, Polygon, Entry
def convert():
    # get user input in celsius
    celsius = eval(input("what is the temperature in celsius?"))
    # covert input from celsius to fahrenheit using the equation c x (9/5) + 32
    fahrenheit = celsius * 9 / 5 + 32
    # display result to user
    print("the temperature is", fahrenheit, " degrees fahrenheit. Awesome!")

def convert_gui():
    win = GraphicWin("Converter", 700, 500)
    win.setCoords(0, 0, 10, 10)
    celsius_text = Text(Point(3, 8), "Celsius")
    celsius_entry= Entry(Point(7, 8), 30)
    click_text = Text(Point(5, 5), "Click to convert")
    result_text = Text(Point(5,1), "")

    celsius_text.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    result_text.draw(win)
    win.getMouse()
    celsius = eval(celsius_entry.getText())
    fahrenheit = celsius * 9 / 5 + 32
    result_text.setText(fahrenheit)
