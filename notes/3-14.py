import math

def my_first_while():
    for i in range(5):
        print(i, end='')
    print('\n{0:-<70}'.format(''))

    i = 0
    while i < 5:
        print(i, end=' ')
        i = i + 1

def is_game_over(player_one_points, player_two_points):
    over_fifteen =  player_one_points or player_two_points >= 15
    won_by_two = abs(player_one_points - player_two_points) >= 2
    skunked = player_one_points >= 7 and player_two_points <= 0 or player_two_points >= 7 and player_one_points == 0
    if over_fifteen and won_by_two or skunked:
        return True
    return False

if __name__ == '__main__':
    player_1 = 10
    player_2 = 12
    while not is_game_over(player_1, player_2):
        one_points, two_points = eval(input('enter points for player 1 and 2: '))
        player_1 = player_1 + one_points
        player_2 = player_2 + two_points
        print(player_1, player_2)
    print("GAME OVER!")
