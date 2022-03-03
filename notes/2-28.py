import math

def convert():
    celsius = eval(input("what is the temperature in celsius"))
    fahrenheit = celsius * (9 / 5) + 32
    print("the temperature is", fahrenheit, "degrees fahrenheit. Awesome ^_^")
    if fahrenheit > 90:
        print("wow that's hot!")
    if fahrenheit < 30:
        print("brrr, that's cold")

def quadratic(a,b,c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print("no real roots")
    else:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b - sqrt_discr) / denom
        print('root 1 :', root_1, 'root 2:', root_2)