"""
Briana Addison
Lab 11
lab11.py

Problem: This code makes a secret door game
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from labs.lab10.door import Door
from labs.lab10.button import Button
from random import randint
from graphics import *


def three_door_game():
    win = GraphWin("Three Door Game", 700, 700)
    win.setBackground("pink")
    quit_button = Button(Rectangle(Point(600, 50), Point(670, 150)), "Quit")
    door_2 = Door(Rectangle(Point(220, 300),Point(420, 500)),"door 2")
    door_1 = Door(Rectangle(Point(10,300),Point(210,500)),"door 1")
    door_3 = Door(Rectangle(Point(430,300),Point(630,500)),"door 3")
    door_1.draw(win)
    door_1.get_label().draw(win)
    door_1.color_door(color_rgb(138,54,15))
    door_2.draw(win)
    door_2.get_label().draw(win)
    door_2.color_door(color_rgb(138,54,15))
    door_3.draw(win)
    door_3.get_label().draw(win)
    door_3.color_door(color_rgb(138,54,15))
    quit_button.draw(win)
    quit_button.get_label().draw(win)


    win_counter = 0
    lose_counter = 0
    win_display = Rectangle(Point(0, 50), Point(100, 150))
    lose_display = Rectangle(Point(100, 50), Point(200,150))
    winning_text = Text(Point(80,100), win_counter)
    losing_text = Text(Point(150,100),lose_counter)
    win_display.draw(win)
    winning_text.draw(win)
    lose_display.draw(win)
    losing_text.draw(win)

    secret_door = Text(Point(350, 150), "I have a secret door")
    guess_message = Text(Point(350, 600), "Click to guess which is the secret door!")
    secret_door.draw(win)
    guess_message.draw(win)




    door_num_gen = randint(1, 3)
    print(door_num_gen)
    if door_num_gen == 1 :
        door_1.set_secret(True)
    elif door_num_gen == 2:
        door_2.set_secret(True)
    elif door_num_gen == 3:
        door_3.set_secret(True)

    user_click = win.getMouse()

    while door_1.is_clicked(user_click) == True:
        while door_1.is_secret():
            door_1.color_door("green")
            win_counter = win_counter + 1
            winning_text.setText(win_counter)
            secret_door.setText("you win!")
        else:
            door_1.color_door("red")
            lose_counter = lose_counter + 1
            losing_text.setText(lose_counter)
            secret_door.setText("sorry, incorrect :(")
    while door_2.is_clicked(user_click) == True:
        while door_2.is_secret():
            door_2.color_door("green")
            win_counter = win_counter + 1
            winning_text.setText(win_counter)
            secret_door.setText("you win!")
        else:
            door_2.color_door("red")
            lose_counter = lose_counter + 1
            losing_text.setText(lose_counter)
            secret_door.setText("sorry, incorrect :(")
    while door_3.is_clicked(user_click) == True:
        while door_3.is_secret():
            door_3.color_door("green")
            win_counter = win_counter + 1
            winning_text.setText(win_counter)
            secret_door.setText("you win!")
        else:
            door_3.color_door("red")
            lose_counter = lose_counter + 1
            losing_text.setText(lose_counter)
            secret_door.setText("sorry, incorrect :(")

    user_click = win.getMouse()
    while quit_button.is_clicked(user_click):
        win.close()









