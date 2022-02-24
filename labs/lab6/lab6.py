"""
Name: Briana Addison
lab6.py

Problem: This program makes a Vigenere cipher in graphic

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *


def vigenere():
    message = ""
    win = GraphWin("vigenere",700, 500 )
    win.setBackground("light gray")
    prompt_message = Text(Point(200, 100), "Message to code: ")
    prompt_keyword = Text(Point(200, 200), "Enter Keyword: ")
    message_box = Entry(Point(400, 100), 30)
    keyword_box = Entry(Point(350, 200), 30)
    encode_box = Rectangle(Point (300, 250), Point(450, 350))
    encode_box_text = Text(Point(380,300), "Encode")

    win.getMouse()








    message_box.setFill("pink")
    keyword_box.setFill("pink")
    encode_box.setFill("pink")
    encode_box_text.setSize(18)
    encode_box.draw(win)
    message_box.draw(win)
    keyword_box.draw(win)
    prompt_message.draw(win)
    prompt_keyword.draw(win)
    encode_box_text.draw(win)
    win.getMouse()


    user_message = message_box.getText()
    user_keyword = keyword_box.getText()
    encode_box.undraw()
    encode_box_text.undraw()




    for i in range (len(user_message)):
        translate_message = user_message[i]
        translate_message = ord(translate_message) -65
        key_length = ord(user_keyword[i%len(user_keyword)]) - 65
        asc_message = (key_length + translate_message)%26
        asc_message = asc_message + 65
        final_message = chr(asc_message)
        message = message[:] + final_message


    display_final = Text(Point(350, 400), final_message + message[:])
    display_final.draw(win)
    display_final.setSize(24)
    print(final_message + message[:])



    win.getMouse()
    win.close()

