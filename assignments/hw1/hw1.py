"""
Name: Briana Addison
hw1.py

Problem: I am solving multiple problems by using user input


I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
   length = eval(input("Enter the length: "))
   width =  eval(input("Enter the width: "))
   height =  eval(input("Enter the height: "))
   volume = length * width * height
   print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    player_shots = eval(input("Enter how many shots the player made: "))
    shooting_percentage = total_shots * player_shots
    print("Shooting Percentage:", shooting_percentage, "%")


def coffee():
    coffee_cost_pound = 10.50
    coffee_shipping = 0.86
    coffee_fixed_price = 1.50
    num_of_pounds = eval(input("How many pounds of coffee would you like?"))
    coffee_total = (coffee_cost_pound * num_of_pounds) + (coffee_shipping * num_of_pounds ) + (coffee_fixed_price)
    print("Your total is: $", coffee_total)



def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers * 0.62111801

    print("That's", round(miles, 2), "miles!")


if __name__ == '__main__':
    pass
