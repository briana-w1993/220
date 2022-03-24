"""
Name: <Briana Addison>
<lab_9>.py
Problem: This code makes a tic tac toe game
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return nums


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(
            v)
    for i in range(
            len(
                    board)):
        if str(
                board[i]).find(
                'x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(
                board[i]).find(
                'o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(
        new_board[0],
        new_board[1],
        new_board[2])
    row_2 = row_format.format(
        new_board[3],
        new_board[4],
        new_board[5])
    row_3 = row_format.format(
        new_board[6],
        new_board[7],
        new_board[8])
    row_separator = '-' * 11
    print(
        LIGHT_GRAY)
    print(
        row_1)
    print(
        row_separator)
    print(
        row_2)
    print(
        row_separator)
    print(
        row_3)
    print(
        reset)


def is_legal(board,position):
    fill_space = position - 1
    tic_tac = board[fill_space]
    if str(tic_tac).isnumeric():
        return True
    else:
        return False


def fill_spot(board,position,character):
    board[position - 1] = character
    board[position - 1].strip()
    board[position - 1].lower()




def winning_game(board):
    if board[0] and board[6] and board[3] == True:
        return True
    elif board[1] and board[4] and board[7] == True:
        return True
    elif board[2] and board[5] and board[8] == True:
        return True
    elif board[0] and board[1] and board[2] == True:
        return True
    elif board[3] and board[4] and board[5] == True:
        return True
    elif board[6] and board[7] and board[8] == True:
        return True
    elif board[0] and board[4] and board[8] == True:
        return True
    elif board[2] and board[4] and board[6] == True:
        return True
    else:
        return False

def game_over(board):
    if winning_game(board):
        return True
    for i in board:
        if i != str(board).isnumeric():
            return False
        else:
            return True



def get_winner(board):
    x = board.count("x")
    o = board.count("o")
    if x > o:
        return "x"
    elif o > x:
        return "o"


def play(board):
    if game_over(board) == True and get_winner(board) == "x":
        return "x's win"
    elif game_over(board) == True and get_winner(board) == "o":
        return "o's win!"



def main():
    char_x = "x"
    char_o = "o"
    while game_over(build_board()) == False:
        print_board(build_board())
        play(build_board())
        x = eval(input("x's choose a position: "))
        fill_spot(build_board(),x, char_x )
        print_board(build_board())
        o = eval(input("o's choose a position"))
        fill_spot(build_board(), o, char_o)
        print_board(build_board())
        is_legal(build_board(), x or o)
        winning_game(build_board())
        game_over(build_board())
        get_winner(build_board())



if __name__ == '__main__':
    main()
