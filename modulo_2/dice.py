import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

d6 = Die()
d10 = Die(10)
d20 = Die(20)

for _ in range(10):
    print("D6:", d6.roll_die(), "D10:", d10.roll_die(), "D20:", d20.roll_die())
