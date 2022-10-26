from game_classes.human import Human
import random

class Begger(Human):
    def __init__(self)
        super().__init__()
        self.name = "Some Begger"
        self.armor = 1 
        self.mana = 1
        self.strength = 12

    def defend(self, damage):
        roll = random.randint(1,6)
        if roll == 6:
            print(f"{self.name} avoids all damage")
        else:
            super().defend(damage)