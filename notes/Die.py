from random import randint

class Die:
    #constuctor
    def __init__(self, num_sides ):
        self.sides = num_sides
        self.value = 1
    def get_value(self):
        return self.value
    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value

    






    #methods

    def main(self):
        d = Die(6)
        d.roll()
        print(d.get.value())
