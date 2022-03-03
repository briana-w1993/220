# days = ["mon", "tues", "wed", "thurs", "fri"]
# for i in range (100):
#     print(days[i%5])
#
# x = 8
# y = (x%9)
# print(y)

def user_names():
    first = input("Enter your first name:")
    last = input("Enter last name:")
    first_letter = first[0]
    last_seven = last[0:7]
    username = first_letter + last_seven
    print("username:", username)

def get_month():
    months = "JanFebMarAprMayJunJulAugSepNovDec"
    month_num = eval(input("Enter a month #"))
    month = months[month_num :3]
    print("that is " , month)