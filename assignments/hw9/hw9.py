"""
Briana Addison
Homework 9
hw9.py

Problem: This code makes a hangman game
Certification of Authenticity:
I certify that this assignment is entirely my own work , but I discussed it
with: Brooke.
"""

from random import randint
from graphics import *


guesses = 6
def get_words(file_name):
    file = open(file_name, "r")
    return file.readlines()



def get_random_word(words):
    num_words = randint(0,len(words) - 1 )

    return words[num_words]


def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if i is letter:
            print(True)
    else:
        return False


def already_guessed(letter, guesses):
    for i in guesses:
        if i is letter:
            print(True)
    else:
        return False




def make_hidden_secret(secret_word, guesses):
    guess = []
    for i in range(len(secret_word)):
        guess.append("_ ")
    for j in range(len(secret_word)):
        letter = secret_word[j]
        for k in guesses:
            if k == letter:
                guess[j] = letter + " "

    return "".join(guess)





def won(guessed):
    for i in range(len(guessed)):
        if guessed[i] == "_":
            return False
    return True




def play_graphics(secret_word):

    win = GraphWin("Hangman", 500, 500)
    win.setBackground("white")
    stick_one = Line(Point(250, 400), Point(250,100))
    stick_one.draw(win)

    stick_two = Line(Point(140, 400), Point(310, 400))
    stick_two.draw(win)

    stick_three = Line(Point(250, 100), Point(140, 165))
    stick_three.draw(win)

    stick_four = Line(Point(140, 100), Point(140, 100))
    stick_four.draw(win)

    #letters

    a = Text(Point(410, 20), "a")
    a.draw(win)

    b = Text(Point(410, 40), "b" )
    b.draw(win)

    c = Text(Point(410, 60),"c")
    c.draw(win)

    d = Text(Point(410, 80), "d")
    d.draw(win)
    e = Text(Point(410, 100), "e" )
    e.draw(win)
    f = Text(Point(410, 120),"f")
    f.draw(win)
    g = Text(Point(410, 140),"g")
    g.draw(win)
    h = Text(Point(410, 160),"h")
    h.draw(win)
    i = Text(Point(410, 180),"i")
    i.draw(win)
    j = Text(Point(410, 200),"j")
    j.draw(win)
    k = Text(Point(410, 220),"k")
    k.draw(win)
    l = Text(Point(410, 240),"l")
    l.draw(win)
    m = Text(Point(410, 260),"m")
    m.draw(win)
    n = Text(Point(430, 20),"n")
    n.draw(win)
    o = Text(Point(430, 40),"o")
    o.draw(win)
    p = Text(Point(430, 60),"p")
    p.draw(win)
    q = Text(Point(430, 80),"q")
    q.draw(win)
    r = Text(Point(430, 100),"r")
    r.draw(win)
    s = Text(Point(430, 120),"s")
    s.draw(win)
    t = Text(Point(430, 140),"t")
    t.draw(win)
    u = Text(Point(430, 160),"u")
    u.draw(win)
    v = Text(Point(430, 180),"v" )
    v.draw(win)
    w = Text(Point(430, 200),"w")
    w.draw(win)
    x = Text(Point(430, 220),"x")
    x.draw(win)
    y = Text(Point(430, 240),"y")
    y.draw(win)
    z = Text(Point(430, 260),"z")
    z.draw(win)

    win.getMouse()


    input_box = Entry(Point(430, 315), 5)





    guesses = 6
    letter_guesses = []
    print("guesses remaining: ",guesses)
    while guesses > 0 and not won(
            make_hidden_secret(
                    secret_word,
                    letter_guesses)):
        input_box.draw(win)
        print(
            "already guessed:",
            letter_guesses)
        Text(Point(350,415),make_hidden_secret(secret_word,letter_guesses))

        guess = input(
            "guess a letter")
        letter_guesses.append(
            guess)
        letter_in_secret_word(
            guess,
            secret_word)
    if letter_in_secret_word(
            letter_guesses,
            secret_word) == True:
        guesses = 6
        print(
            "guesses remaining: ",
            guesses)

    if letter_in_secret_word(
            letter_guesses,
            secret_word) == False:
        guesses = guesses - 1
        print(
            "guesses remaining:",
            guesses)
    if won(
            make_hidden_secret(
                    secret_word,
                    letter_guesses)):
        print(
            "Winner!!")
    else:
        print(
            "You lost :(",
            "the correct word was",
            secret_word)



    if guesses == 5:
        head = Circle(Point(140, 190), 25)
        head.draw(win)
    if guesses == 4:
        body = Line(Point(140, 190), Point(140, 355))
        body.draw(win)
    if guesses == 3:
        left_arm = Line(Point(140, 215), Point(80, 250))
        left_arm.draw(win)

    if guesses == 2:
        right_arm = Line(Point(140, 215), Point(200, 250))
        right_arm.draw(win)
    if guesses == 1:
        left_leg = Line(Point(140, 355), Point(90, 390))
        left_leg.draw(win)
    if guesses == 0:
        right_leg = Line(Point(140, 355), Point(190, 390))
        right_leg.draw(win)
        Text(Point(350, 100),"You lost :(. the correct word was" +
             secret_word)



    win.getMouse()
    win.getMouse()



    win.close()


def play_command_line(secret_word):
    guesses = 6
    letter_guesses = []
    print("guesses remaining: ",guesses)
    while guesses > 0 and not won(make_hidden_secret(secret_word, letter_guesses)):

        print("already guessed:", letter_guesses)
        print(make_hidden_secret(secret_word, letter_guesses))

        guess = input("guess a letter")
        letter_guesses.append(guess)
        letter_in_secret_word(guess, secret_word)
    if letter_in_secret_word(letter_guesses,secret_word) == True:
        guesses= 6
        print("guesses remaining: ", guesses)

    if letter_in_secret_word(letter_guesses, secret_word) == False:
        guesses_f = guesses - 1
        print("guesses remaining:",guesses_f)
    if won(make_hidden_secret(secret_word,letter_guesses)):
        print("Winner!!")
    else:
        print("You lost :(", "the correct word was", secret_word)








if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
