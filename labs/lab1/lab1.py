"""
Briana Addison
Lab 1
Monthly Interest
Problem: This code solves the problem of finding the monthly interest
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def monthly_interest():
    print("Monthly Interest")
    # annual interest rate
    annual_interest = eval(input("What is your annual interest rate?"))
    # number of days in the billing cycle
    num_of_days = eval(input("How many days are in your billing cycle?"))
    # previous net balance
    prev_net_balance = eval(input("What was your previous net balance?"))
    # payment amount
    payment_amount = eval(input("What was the amount that you payed?"))
    # day of the billing cycle in which the payment was made
    day_of_billing = eval(input("What is the day of the billing cycle in which the payment was made?"))
    step_1 = prev_net_balance * num_of_days
    step_2 =  (num_of_days - day_of_billing) * payment_amount
    step_3 = step_1 - step_2
    step_4 =  step_3 / num_of_days
    final= round(step_4, 2)
    print("Your average daily is $", final, "!")
    monthly_interest_rate = (annual_interest / 12) / 100
    fin_balance = final * monthly_interest_rate
    fin_balance_rounded =  round(fin_balance, 2)
    print("Your monthly interest is $", fin_balance_rounded)
