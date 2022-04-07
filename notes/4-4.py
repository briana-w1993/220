def avg():
    acc = []

    user_input = 0
    while user_input!= "":
        acc = acc +[eval(user_input)]

        user_input = input("enter #(enter to quit)")
    return acc

def funzies():
    a = [4,5,6]
    for i in a:
        i = 7
        print(i)
    for i in range(len(a)):
        a[i] = 7
        print(a[i])
