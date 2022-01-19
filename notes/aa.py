
def convert():
    # get user input in celsius
    celsius = eval(input("what is the temperature in celsius?"))
    # covert input from celsius to fahrenheit using the equation c x (9/5) + 32
    fahrenheit = celsius * 9 / 5 + 32
    # display result to user
    print("the temperature is", fahrenheit, " degrees fahrenheit. Awesome!")
